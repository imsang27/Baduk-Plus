---
Date_of_creation: 2025-06-05 목 22:05:36
Last_modified:
  - 2025-06-09 월 03:47:00
  - 2025-06-07 토 22:03:43
  - 2025-06-05 목 22:27:59
  - "2025-06-04 수 15: 01:41"
  - "2025-06-02 월 13: 29:55"
aliases: 
tags: 
Reference: 
---
# 🧩 프로젝트명
---
**Baduk Plus – 실시간 바둑 대국 기록 및 중계 시스템**

# 1. 프로젝트 개요
---
Baduk Plus는 바둑 대국의 모든 정보를 Firebase에 저장하고, 그 중 "대국 결과"만 MySQL로 동기화하는 실습 프로젝트입니다.

# 2. 요구사항 요약
---
1. **자신만의 주제를 정한다.**
    - _이 프로젝트의 가장 핵심이 되는 항목입니다._
    - _혼자서 만드는 프로젝트이니 자신만의 색깔을 분명히 나타낼 수 있는 주제로 구성해 주세요._ 
    => [`docs/PRD.md`](https://github.com/imsang27/Baduk-Plus/blob/main/docs/PRD.md), [`docs/README.md`](https://github.com/imsang27/Baduk-Plus/blob/main/docs/README.md)

2. **MySQL과 Firebase를 이용하여 각각 데이터베이스를 구축한다.
    - 두 시스템을 병행하여 구조와 목적의 차이를 체험하는 것이 목표
    => [`MySQL/create_tables.sql`](https://github.com/imsang27/Baduk-Plus/blob/main/MySQL/create_tables.sql), [`Firebase/firebase_structure.json`](https://github.com/imsang27/Baduk-Plus/blob/main/Firebase/firebase_structure.json), [`Firebase/firebase_auth.json`](https://github.com/imsang27/Baduk-Plus/blob/main/Firebase/firebase_auth.json)

3. **MySQL에서는 주제에 따라 스키마를 설계하고, 테이블을 생성한다.**
    - 반드시 ERD를 작성하고, 기본키/외래키/제약조건 등을 포함할 것
    => [`MySQL/create_tables.sql`](https://github.com/imsang27/Baduk-Plus/blob/main/MySQL/create_tables.sql), [`MySQL/mysql_tables.sql`](https://github.com/imsang27/Baduk-Plus/blob/main/MySQL/mysql_tables.sql), [`docs/ERD.md`](https://github.com/imsang27/Baduk-Plus/blob/main/docs/ERD.md)

4. **Firebase에서는 실시간 데이터베이스를 생성하고, 실시간 데이터를 하나 이상 수집·저장하도록 설계한다.**
    - 예: 센서 시뮬레이션, 실시간 채팅, 위치 추적 등
    => [`Firebase/firebase_update.py`](https://github.com/imsang27/Baduk-Plus/blob/main/Firebase/firebase_update.py), [`Firebase/firebase_structure.json`](https://github.com/imsang27/Baduk-Plus/blob/main/Firebase/firebase_structure.json), [`Firebase/firebase_auth.json`](https://github.com/imsang27/Baduk-Plus/blob/main/Firebase/firebase_auth.json)

5. **MySQL과 Firebase의 연동을 자신만의 방식으로 구현한다.**
    - _이 항목은 프로젝트의 도전 과제입니다._
    - 기술 스택은 자유
    => [`Firebase/firebase_mysql_sync.py`](https://github.com/imsang27/Baduk-Plus/blob/main/Firebase/firebase_mysql_sync.py), [`MySQL/mysql_connection.py`](https://github.com/imsang27/Baduk-Plus/blob/main/MySQL/mysql_connection.py), [`Firebase/firebase_auth.json`](https://github.com/imsang27/Baduk-Plus/blob/main/Firebase/firebase_auth.json)

6. **챗봇 또는 외부 프로그램을 활용하여 더미 데이터를 자동 생성·입력한다.**
    - 단순 수동 입력이 아닌 자동화된 더미 데이터 생성 방식을 시도할 것
    - 예: ChatGPT 프롬프트로 JSON 생성 → Firebase에 저장
    => [`Firebase/generate_baduk_gibo.py`](https://github.com/imsang27/Baduk-Plus/blob/main/Firebase/generate_baduk_gibo.py), [`Firebase/dummy data/`](https://github.com/imsang27/Baduk-Plus/tree/main/Firebase/dummy%20data), [`Firebase/firebase_auth.json`](https://github.com/imsang27/Baduk-Plus/blob/main/Firebase/firebase_auth.json)

7. **MySQL에 저장 프로시저를 구현하여 다음 기능을 포함한다.**
    - 데이터 입력
    - 데이터 조회
    - 데이터 삭제
    => [`MySQL/stored_procedures.sql`](https://github.com/imsang27/Baduk-Plus/blob/main/MySQL/stored_procedures.sql), [`MySQL/mysql_connection.py`](https://github.com/imsang27/Baduk-Plus/blob/main/MySQL/mysql_connection.py)

8. **간단한 인터페이스(UI)나 앱을 만들어 실제 데이터를 조회하고 확인할 수 있도록 한다.**
    - 웹 페이지, 모바일 앱, 콘솔 앱 등 어떤 형태든 무관
    - 조회 결과가 시각적으로 확인 가능해야 함
    => [`Interface/app.py`](https://github.com/imsang27/Baduk-Plus/blob/main/Interface/app.py), [`Interface/viewer.html`](https://github.com/imsang27/Baduk-Plus/blob/main/Interface/viewer.html), [`Interface/templates/`](https://github.com/imsang27/Baduk-Plus/tree/main/Interface/templates), [`Interface/js/`](https://github.com/imsang27/Baduk-Plus/tree/main/Interface/js), [`Interface/screenshots/`](https://github.com/imsang27/Baduk-Plus/tree/main/Interface/screenshots)

9. **전체 결과물을 압축하여 이강의동 데이터베이스 구축 프로젝트 과제로 제출한다.**
    - 구성 예시:
        - `/MySQL/` (ERD, 테이블 생성 SQL, 프로시저 등)
        - `/Firebase/` (DB 구조 스크린샷, 연동 코드 등)
        - `/Interface/` (UI 캡처, 설명)
    => [`docs/README.md`](https://github.com/imsang27/Baduk-Plus/blob/main/docs/README.md), [`docs/PRD.md`](https://github.com/imsang27/Baduk-Plus/blob/main/docs/PRD.md), [`docs/ERD.md`](https://github.com/imsang27/Baduk-Plus/blob/main/docs/ERD.md)

# 3. 주요 기능 정의
---

| 기능                        | 설명                                                                 | 기술 요소 |
|-----------------------------|----------------------------------------------------------------------|------------|
| 대국자 등록 및 관리          | 플레이어 이름, 기력, 프로 여부 등 관리                                 | MySQL       |
| 대국 정보 저장              | 대국 일자, 규칙, 기보 이름, 승률, 집차이, 결과 등                      | MySQL       |
| 수순 저장                   | 착점 좌표, 시간, 색상 등 저장                                        | MySQL       |
| 실시간 수순 전송 및 갱신     | Firebase에 실시간으로 착점 데이터 업로드                              | Firebase    |
| 더미 수순 자동 생성         | 랜덤 수순 생성 후 Firebase에 삽입                                     | Python      |
| Firebase ↔ MySQL 연동       | 결과 요약 전송 및 상태 동기화                                        | Python      |
| UI 실시간 관전 뷰어         | Firebase Listener 기반 착점 시각화                                   | HTML/JS     |

# 4. 기술 스택
---

| 분류       | 기술                                |
| -------- | --------------------------------- |
| Backend  | Python (firebase-admin 등)         |
| Database | MySQL, Firebase Realtime Database |
| Frontend | HTML + JS (웹 기반 UI)               |
| 자동화      | Python 기반 더미 생성기 및 연동 스크립트        |
| 문서화      | Markdown, Mermaid (ERD), PDF 보고서  |

# 5. 프로젝트 디렉토리 구성
---
```
baduk-plus/
├── docs          # PRD.md 및 여러 md 파일
├── Firebase/     # 실시간 DB 구조 및 연동 코드
├── Interface/    # 웹 기반 UI 캡처 및 코드
├── MySQL/        # ERD, 테이블, 프로시저
└── README.md
```

# 6. 일정
---
**진행 기간**: 2025년 5월 26일(월) ~ 6월 9일(월), 총 3주간 진행

| 주차  | 기간       | 목표                         |
| --- | -------- | -------------------------- |
| 1주차 | 5/26~6/1 | 주제 확정 및 구조 구상              |
| 2주차 | 6/2~6/7  | MySQL 스키마 + Firebase 구조 완료 |
| 3주차 | 6/8      | 자동화 + 연동 + UI 통합 테스트       |
| 제출일 | 6/9      | 프로젝트 압축 제출                 |

## 데이터 구조

### Firebase
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

### MySQL
```sql
CREATE TABLE game_results (
    game_id VARCHAR(255) PRIMARY KEY,
    result VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```
- **MySQL에는 games/{game_id}/대국 결과만 저장**
