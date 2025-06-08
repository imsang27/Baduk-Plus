import random
import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
import os

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

# 흑/백 대국자 정보
match_data = {
    "players": {
        "black": {"name": "Lee Sedol", "rank": "9단", "is_pro": True},
        "white": {"name": "AlphaGo", "rank": "9단", "is_pro": False}
    },
    "rule": "Chinese",
    "start_time": start_time.isoformat(),
    "moves": {},
    "status": "ongoing"
}

# 초기 match 등록
ref = db.reference(f"matches/{match_id}")
ref.set(match_data)

# 수순 시뮬레이션: 10수만 랜덤 착수
for move_number in range(1, 11):
    x = random.randint(1, 19)
    y = random.randint(1, 19)
    color = "black" if move_number % 2 == 1 else "white"
    timestamp = datetime.now().isoformat()

    move_data = {
        "x": x,
        "y": y,
        "color": color,
        "timestamp": timestamp
    }

    ref.child("moves").child(str(move_number)).set(move_data)
    print(f"{move_number}번째 수: {color} ({x},{y}) - {timestamp}")
    time.sleep(1)

# 결과 저장
result_data = {
    "winner_color": "white",
    "reason": "resign",
    "point_difference": 5.5
}
ref.child("status").set("finished")
ref.child("result").set(result_data)