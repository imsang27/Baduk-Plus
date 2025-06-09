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
├── docs/                    # 문서화 파일
│   ├── erd.mmd.md           # ERD 문서
│   ├── PRD.md               # 프로젝트 요구사항 문서
│   ├── procedures.sql.md    # 저장 프로시저 문서
│   └── schema.sql.md        # 스키마 문서
├── Firebase/                # Firebase 관련 코드
│   ├── firebase_auth.json
│   ├── firebase_mysql_sync.py
│   ├── firebase_update.py
│   └── generate_baduk_gibo.py
├── Interface/               # 웹 인터페이스
│   ├── app.py
│   ├── Screenshot/
│   ├── templates/
│   └── viewer.html
├── MySQL/                   # MySQL 관련 파일
│   ├── create_tables.sql
│   ├── mysql_connection.py
│   ├── mysql_tables.sql
│   └── stored_procedures.sql
├── requirements.txt         # Python 패키지 의존성
└── README.md                # 프로젝트 설명
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