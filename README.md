---
Date_of_creation: 2025-06-02 월 12:49:51
Last_modified:
  - 2025-06-02 월 12:59:49
aliases:
  - DB 구축 프로젝트
  - 데이터베이스 구축 프로젝트
  - 바둑 DB
  - Baduk Plus README
tags:
  - 공부/3학년_1학기/DB설계와_활용
Reference:
---
# Baduk Plus
---
바둑 대국 정보를 실시간으로 추적하고, MySQL과 Firebase 양쪽에 기록하는 실시간 연동 시스템입니다.

## 📘 프로젝트 개요
---
Baduk Plus는 바둑 대국의 수순과 관련 정보를 체계적으로 저장하고, Firebase를 이용해 실시간으로 대국 상황을 중계할 수 있도록 하는 시스템입니다.
이를 통해 데이터의 정형 저장(분석 목적)과 실시간 전송(관전 목적)을 동시에 만족합니다.

## 🧠 프로젝트 목표
---
- MySQL과 Firebase의 구조적 차이와 장단점을 직접 체험
- 실시간 데이터 흐름과 정형 데이터 저장을 동시에 다루는 복합 시스템 설계 경험
- 자동화, 실시간성, UI 등 실제 서비스 구성 요소들을 구현

## 🏗️ 핵심 기능
---

| 기능                    | 설명                                                                 |
|-------------------------|----------------------------------------------------------------------|
| 대국 정보 저장          | 흑/백 대국자, 기력, 날짜, 규칙, 결과, 승률, 집차이 등 MySQL에 저장 |
| 수순 기록               | 각 수의 좌표, 색깔, 착점까지 걸린 시간 등 수순 정보 관리            |
| 실시간 대국 중계        | Firebase를 통해 현재 대국의 수순을 실시간으로 반영                  |
| 더미 데이터 자동 생성   | Python 스크립트를 활용해 랜덤한 기보 자동 생성 및 Firebase 저장     |
| 실시간 UI 조회          | 실시간 대국 상황을 관전할 수 있는 인터페이스 제공                  |
| 데이터 연동             | Firebase ↔ MySQL 간의 정보 동기화 설계                              |

## 🔧 사용 기술
---
- MySQL
- Firebase Realtime Database
- Python
- Mermaid.js
- (선택) 웹 UI: Flask, HTML, JS 등

## 📁 프로젝트 구조
---
```
baduk-Plus/
├── MySQL/
│   ├── erd.mmd
│   ├── schema.sql
│   └── procedures.sql
├── Firebase/
│   ├── simulate_match.py
│   ├── firebase_structure.png
├── Interface/
│   ├── viewer.html
│   └── ui_screenshots/
└── README.md
```

## 💬 한줄 요약
---
> 바둑 대국의 흐름을 실시간으로 추적하고 기록하는 이중 데이터베이스 기반의 실시간 연동 시스템입니다.
