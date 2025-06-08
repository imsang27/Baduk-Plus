import json
import random
from datetime import datetime

def num_to_korean_coord(x, y):
    x_labels = [chr(i) for i in range(ord('A'), ord('T')+1) if i != ord('I')]
    return f"{x_labels[x - 1]}-{y}"

def generate_dummy_gibo(num_moves=20):
    gibo = {}
    for move_num in range(1, num_moves + 1):
        x = random.randint(1, 19)
        y = random.randint(1, 19)
        move = {
            "좌표": num_to_korean_coord(x, y),
            "차례": "흑" if move_num % 2 == 1 else "백"
        }
        gibo[str(move_num)] = move
    return gibo

if __name__ == "__main__":
    baduk_game = {
        "기전명": "dummy_대국_001",
        "대국자": {
            "흑": { "이름": "흑번", "기력": "초단", "프로기사": False },
            "백": { "이름": "백번", "기력": "2단", "프로기사": False }
        },
        "대국 규칙": "한국룰",
        "대국 시작시간": datetime.now().isoformat(),
        "기보": generate_dummy_gibo(10),
        "대국 상태": "종료",
        "대국 결과": {
            "승자": "흑",
            "승리 방식": "집계승",
            "집차이": 4.5
        }
    }

    with open("더미_기보.json", "w", encoding="utf-8") as f:
        json.dump(baduk_game, f, ensure_ascii=False, indent=2)

    print("더미_기보.json 파일이 생성되었습니다.")