import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
import os
from datetime import datetime
from generate_baduk_gibo import generate_rule_info, generate_time_settings, generate_game_result, generate_dummy_gibo, generate_num_moves
import random

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

# 더미 대국 정보 생성
match_id = f"더미_대국_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
rule_info = generate_rule_info()
time_settings = generate_time_settings()
num_moves = generate_num_moves()  # generate_baduk_gibo.py의 함수 사용

baduk_game = {
    "기전명": match_id,
    "대국자": {
        "흑": { "이름": "Lee Sedol", "기력": "9단", "프로기사": True },
        "백": { "이름": "AlphaGo", "기력": "9단", "프로기사": False }
    },
    "대국 규칙": {
        "룰": rule_info["룰"],
        "덤": rule_info["덤"],
        "시간 설정": {
            "제한시간": time_settings["제한시간"],
            "초읽기": time_settings["초읽기"]
        }
    },
    "수순": generate_dummy_gibo(num_moves),
    "대국 상태": "종료",
    "대국 결과": generate_game_result(num_moves)  # 수순 개수를 전달
}

# Firebase에 저장
ref = db.reference(f"기보/{match_id}")
ref.set(baduk_game)
print(f"Firebase에 더미 대국 데이터가 저장되었습니다. (기전명: {match_id})")