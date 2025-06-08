import random
import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
import os
from generate_baduk_gibo import generate_rule_info, generate_time_settings, generate_game_result, generate_dummy_gibo

load_dotenv()
FIREBASE_DB_URL = os.getenv("FIREBASE_DB_URL")

# Firebase 인증 및 초기화
try:
    cred = credentials.Certificate("./firebase_auth.json")
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred, {
            "databaseURL": FIREBASE_DB_URL
        })
    print("✅ Firebase 초기화 성공")
except Exception as e:
    print("❌ Firebase 초기화 실패:", e)
    exit(1)

# 시뮬레이션할 매치 ID
match_id = "game_20250604_001"

# 시작 시간 기준
start_time = datetime.now()

# 게임 규칙 및 설정 생성
rule_info = generate_rule_info()
time_info = generate_time_settings()
result_info = generate_game_result()
num_moves = random.randint(10, 15)

# 흑/백 대국자 정보
match_data = {
    "players": {
        "black": {"name": "Lee Sedol", "rank": "9단", "is_pro": True},
        "white": {"name": "AlphaGo", "rank": "9단", "is_pro": False}
    },
    "rule": rule_info["룰"],
    "komi": rule_info["덤"],
    "time_settings": {
        "main_time": time_info["제한시간"],
        "byo_yomi": time_info["초읽기"]
    },
    "start_time": start_time.isoformat(),
    "moves": {},
    "status": "ongoing"
}

# 초기 match 등록
ref = db.reference(f"matches/{match_id}")
ref.set(match_data)

# 기보 생성 및 저장
gibo = generate_dummy_gibo(num_moves)
for move_number, move_data in gibo.items():
    x, y = move_data["좌표"].split("-")
    x = ord(x) - ord('A') + 1
    y = int(y)
    color = "black" if move_data["차례"] == "흑" else "white"
    timestamp = datetime.now().isoformat()

    move_info = {
        "x": x,
        "y": y,
        "color": color,
        "timestamp": timestamp
    }

    ref.child("moves").child(move_number).set(move_info)
    print(f"{move_number}번째 수: {color} ({x},{y}) - {timestamp}")
    time.sleep(1)

# 결과 저장
result_data = {
    "winner_color": "white" if result_info["승자"] == "백" else "black",
    "reason": result_info["승리_방식"],
    "point_difference": result_info["집차이"]
}
ref.child("status").set("finished")
ref.child("result").set(result_data)