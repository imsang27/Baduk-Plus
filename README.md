---
Date_of_creation: 2025-06-02 월 12:49:51
Last_modified:
  - 2025-06-08 일 13:08:55
  - 2025-06-04 수 15:06:48
  - 2025-06-02 월 13:19:58
aliases:
  - DB 구축 프로젝트
  - 데이터베이스 구축 프로젝트
  - 바둑 DB
  - Baduk Plus README
tags:
  - 공부/3학년_1학기/DB설계와_활용
Reference: 
---
# Baduk-Plus

이 프로젝트는 바둑 대국의 모든 정보를 Firebase에 저장하고, 그 중 "대국 결과"만 MySQL로 동기화하는 실습 프로젝트입니다.

## 📘 프로젝트 개요
---
Baduk Plus는 바둑 대국의 수순과 관련 정보를 체계적으로 저장하고, Firebase를 이용해 실시간으로 대국 상황을 중계할 수 있도록 하는 시스템입니다.
이 프로젝트는 MySQL과 Firebase의 구조적 차이를 체험하며, 데이터 설계 및 연동 능력을 동시에 기르는 데 목적이 있습니다.

## 🧠 프로젝트 목표
---
1. 자신만의 주제를 바탕으로 실시간 + 정형 데이터 시스템 구현
2. MySQL과 Firebase의 구조와 목적의 차이를 직접 체험
3. Python을 활용하여 양쪽 시스템을 연동
4. 자동화된 더미 데이터 생성 및 저장 처리
5. 웹 기반의 시각적 인터페이스(UI) 구현

## 🏗️ 핵심 기능
---

| 기능                    | 설명                                                                 |
|-------------------------|----------------------------------------------------------------------|
| 대국 정보 저장          | 흑/백 대국자, 기력, 날짜, 규칙, 결과, 승률, 집차이 등 MySQL에 저장 |
| 수순 기록               | 각 수의 좌표, 색깔, 착점까지 걸린 시간 등 수순 정보 관리            |
| 실시간 대국 중계        | Firebase를 통해 현재 대국의 수순을 실시간으로 반영                  |
| 더미 데이터 자동 생성   | Python 스크립트를 활용해 랜덤한 기보 자동 생성 및 Firebase 저장     |
| 실시간 UI 조회          | 웹 브라우저에서 대국 상황을 실시간 관전 가능                        |
| 데이터 연동             | Firebase ↔ MySQL 간의 정보 동기화 설계                              |

## 🔧 사용 기술
---
- MySQL (ERD, 프로시저, 제약조건 포함)
- Firebase Realtime Database
- Python (firebase-admin, mysql-connector-python 등)
- HTML + JS (웹 UI)
- Mermaid.js (ERD 시각화)

## 📁 프로젝트 구조
---
```
Baduk-Plus/
├── Firebase/   # DB 구조 스크린샷, 연동 코드 등
│   ├── firebase_mysql_sync.py
│   ├── firebase_update.py
│   ├── generate_baduk_gibo.py
│   ├── firebase_structure.json
│   └── ...
├── MySQL/      # ERD, 테이블 생성 SQL, 프로시저 등 등
│   ├── mysql_tables.sql
│   └── mysql_connection.py
└── README.md
```

## 💬 한줄 요약
---
> 바둑 대국의 흐름을 실시간으로 추적하고 기록하는 이중 데이터베이스 기반의 실시간 연동 시스템입니다.

## ✅ Baduk Plus 프로젝트 TODO 리스트

### 🧩 1. 기본 설계 및 문서화
- [x] 주제 선정: 바둑 대국 실시간 기록 및 중계
- [x] README 작성 ([`README.md`](https://github.com/imsang27/Baduk-Plus/blob/main/README.md))
- [x] PRD 작성 (요구사항 + 일정 포함) ([`docs/PRD.md`](https://github.com/imsang27/Baduk-Plus/blob/main/docs/PRD.md))
- [x] 디렉토리 구조 명확화

### 🗃️ 2. MySQL 구축
- [x] ERD 설계 ([`docs/ERD.md`](https://github.com/imsang27/Baduk-Plus/blob/main/docs/ERD.md))
- [x] 테이블 생성 스크립트 작성 ([`MySQL/create_tables.sql`](https://github.com/imsang27/Baduk-Plus/blob/main/MySQL/create_tables.sql), [`MySQL/mysql_tables.sql`](https://github.com/imsang27/Baduk-Plus/blob/main/MySQL/mysql_tables.sql))
	- [x] 기본키 / 외래키 / 제약조건 등 포함
- [x] 저장 프로시저 작성 ([`MySQL/stored_procedures.sql`](https://github.com/imsang27/Baduk-Plus/blob/main/MySQL/stored_procedures.sql))
- [x] MySQL 연결 설정 ([`MySQL/mysql_connection.py`](https://github.com/imsang27/Baduk-Plus/blob/main/MySQL/mysql_connection.py))
- [ ] ERD → PDF로 시각화 (선택사항)

### 🔥 3. Firebase 구축
- [x] 실시간 DB 구조 설계 ([`Firebase/firebase_structure.json`](https://github.com/imsang27/Baduk-Plus/blob/main/Firebase/firebase_structure.json))
- [x] 구조 시각화 자료 제작 ([`Firebase/firebase_structure.json`](https://github.com/imsang27/Baduk-Plus/blob/main/Firebase/firebase_structure.json))
- [x] Python을 이용한 Firebase 업데이트 코드 구현 ([`Firebase/firebase_update.py`](https://github.com/imsang27/Baduk-Plus/blob/main/Firebase/firebase_update.py))

### 🔄 4. 연동 및 자동화
- [x] 더미 데이터 생성 스크립트 작성 ([`Firebase/generate_baduk_gibo.py`](https://github.com/imsang27/Baduk-Plus/blob/main/Firebase/generate_baduk_gibo.py))
- [x] Firebase에 더미 수순 자동 삽입 ([`Firebase/firebase_update.py`](https://github.com/imsang27/Baduk-Plus/blob/main/Firebase/firebase_update.py))
- [x] MySQL-Firebase 간 연동 구현 ([`Firebase/firebase_mysql_sync.py`](https://github.com/imsang27/Baduk-Plus/blob/main/Firebase/firebase_mysql_sync.py))
- [x] 양방향 상태 동기화 구현 (예: 결과 요약 동기화)

### 👁️ 5. 시각화 및 UI
- [x] 실시간 UI 구현 ([`Interface/viewer.html`](https://github.com/imsang27/Baduk-Plus/blob/main/Interface/viewer.html))
- [ ] UI 시각자료 정리 ([`Interface/screenshots/`](https://github.com/imsang27/Baduk-Plus/tree/main/Interface/screenshots))
- [x] Firebase Listener로 수순 업데이트 UI 동기화
- [x] Flask 기반 웹 서버 구현 ([`Interface/app.py`](https://github.com/imsang27/Baduk-Plus/blob/main/Interface/app.py))

### 📦 6. 최종 제출 준비
- [ ] 전체 프로젝트 압축(zip)
- [ ] 불필요한 파일 정리 (.log, 테스트용 데이터 등)
- [ ] 시연 영상 또는 스크린샷 포함 (선택)
- [ ] 제출 전 기능 점검 완료

## MySQL 연결 설정

Firebase와 MySQL 연동을 위해 다음 환경 변수들을 설정해야 합니다:

1. `.env` 파일을 프로젝트 루트 디렉토리에 생성하고 다음 변수들을 설정하세요:

```
MYSQL_HOST = your_mysql_host
MYSQL_DATABASE = your_database_name
MYSQL_USER = your_username
MYSQL_PASSWORD = your_password
```

2. 필요한 Python 패키지 설치:
```bash
pip install mysql-connector-python python-dotenv
```

## ERD/테이블 구조

- MySQL: `game_results` 테이블 (game_id, result, created_at)
- Firebase: games/{game_id}/대국 결과

## 예시 데이터 구조

Firebase:
```json
{
  "games": {
    "20240609_001": {
      "기전명": "더미_대국_20240609_001",
      "대국자": {
        "흑": { "이름": "Lee Sedol", "기력": "9단", "프로기사": true },
        "백": { "이름": "AlphaGo", "기력": "9단", "프로기사": false }
      },
      "대국 규칙": {
        "룰": "한국룰",
        "덤": "흑 공제 6.5집",
        "시간 설정": {
          "제한시간": "2시간 30분",
          "초읽기": "30초 초읽기 3번"
        }
      },
      "수순": { ... },
      "대국 상태": "종료",
      "대국 결과": {
        "승자": "흑",
        "승리_방식": "집계승",
        "집차이": "2.5집",
        "총수순": "150수"
      }
    }
  }
}
```

MySQL:
```sql
CREATE TABLE game_results (
    game_id VARCHAR(255) PRIMARY KEY,
    result VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```
