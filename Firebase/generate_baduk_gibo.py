import json
import random
from datetime import datetime

def num_to_korean_coord(x, y):
    x_labels = [chr(i) for i in range(ord('A'), ord('T')+1) if i != ord('I')]
    return f"{x_labels[x - 1]}-{y}"

def generate_rule_info():
    rules = [
        {"룰": "한국룰", "덤": "흑 공제 6.5집"},
        {"룰": "중국룰", "덤": "흑 공제 7.5집"},
        {"룰": "정선", "덤": "덤 없음"}
    ]
    return random.choice(rules)

def generate_time_settings():
    time_settings = [
        {
            "제한시간": f"{random.randint(1, 3)}시간 {random.randint(0, 1) * 30}분",
            "초읽기": f"{random.randint(3, 6) * 10}초 초읽기 {random.randint(3, 5)}번"
        },
        {
            "제한시간": "피셔룰",
            "초읽기": f"기본시간 {random.randint(1, 3) * 30}분 + {random.randint(3, 6) * 10}초"
        }
    ]
    return random.choice(time_settings)

def generate_game_result():
    winner = random.choice(["흑", "백"])
    win_type = random.choice(["집계승", "불계승", "시간승"])
    if win_type == "집계승":
        score = random.choice([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5])
        result = f"{score}집"
    elif win_type == "시간승":
        result = f"{winner}시간승"
    else:
        result = "불계승"
    return {
        "승자": winner,
        "승리_방식": win_type,
        "집차이": result
    }

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
    rule_info = generate_rule_info()
    time_info = generate_time_settings()
    result_info = generate_game_result()
    num_moves = random.randint(10, 15)

    baduk_game = {
        "기전명": "dummy_대국_001",
        "대국자": {
            "흑": { "이름": "흑번", "기력": "초단", "프로기사": False },
            "백": { "이름": "백번", "기력": "2단", "프로기사": False }
        },
        "대국 규칙": rule_info["룰"],
        "덤": rule_info["덤"],
        "제한시간": time_info["제한시간"],
        "초읽기": time_info["초읽기"],
        "대국 시작시간": datetime.now().isoformat(),
        "기보": generate_dummy_gibo(num_moves),
        "대국 상태": "종료",
        "대국 결과": result_info,
        "총수순": f"{num_moves}수"
    }

    with open("더미_기보.json", "w", encoding="utf-8") as f:
        json.dump(baduk_game, f, ensure_ascii=False, indent=2)

    print("더미_기보.json 파일이 생성되었습니다.")