# Product Requirements Document (PRD)

## 🧩 프로젝트명
**Baduk Sync – 실시간 바둑 대국 기록 및 중계 시스템**

## 1. 프로젝트 개요
Baduk Sync는 바둑 대국 정보를 MySQL에 체계적으로 저장하고, 대국의 수순 진행 상황을 Firebase Realtime Database를 통해 실시간 중계할 수 있도록 하는 시스템입니다.  
이 시스템은 데이터의 정형 저장(분석 목적)과 실시간 전송(관전 목적)을 동시에 충족시키며, 두 데이터베이스의 구조적 차이와 활용 목적을 비교하고 실습하는 데 초점을 둡니다.

## 2. 문제 정의 및 배경
바둑은 각 수순의 착점 위치, 시간, 플레이어 정보 등 다양한 정형/비정형 데이터를 포함한 복잡한 게임입니다. 이러한 데이터를 실시간으로 전달하고 분석할 수 있는 구조를 만드는 것은 실무 시스템에서도 중요한 과제입니다.

## 3. 주요 목표

| 항목                     | 설명 |
|--------------------------|------|
| 🎯 MySQL 스키마 설계       | 대국자, 대국 정보, 수순 테이블 구성. 제약조건 포함 |
| 🎯 Firebase 구조 설계     | 실시간 대국 트리 구성. 좌표, 색상, 시간 등 포함 |
| 🎯 데이터 연동             | 실시간 수순 → Firebase 기록, 결과 요약 → MySQL 저장 |
| 🎯 더미 데이터 자동 생성   | Python 스크립트로 기보 자동 생성 및 저장 |
| 🎯 UI/관전 인터페이스 구현 | 실시간 대국 진행 시각화 페이지 구현 |

## 4. 대상 사용자

- 바둑 동호인 또는 앱 사용자
- 실시간 관전 서비스 구축이 필요한 개발자
- 데이터베이스 구조/연동 실습을 하는 학생 또는 연구자

## 5. 주요 기능 정의

| 기능                        | 설명                                                                 | 기술 요소 |
|-----------------------------|----------------------------------------------------------------------|------------|
| 대국자 등록 및 관리          | 플레이어 이름, 기력, 프로 여부 등 관리                                 | MySQL       |
| 대국 정보 저장              | 대국 일자, 규칙, 기보 이름, 승률, 집차이, 결과 등                      | MySQL       |
| 수순 저장                   | 착점 좌표, 시간, 색상 등 저장                                        | MySQL       |
| 실시간 수순 전송 및 갱신     | Firebase에 실시간으로 착점 데이터 업로드                              | Firebase    |
| 더미 수순 자동 생성         | 랜덤 수순 생성 후 Firebase에 삽입                                     | Python      |
| Firebase ↔ MySQL 연동       | 결과 요약 전송 및 상태 동기화                                        | Python/API |
| UI 실시간 관전 뷰어         | Firebase Listener 기반 착점 시각화                                   | HTML/JS     |

## 6. 기술 스택

| 분류           | 기술                     |
|----------------|--------------------------|
| Backend        | Python (firebase-admin, pymysql 등) |
| Database       | MySQL, Firebase Realtime Database |
| Frontend (선택)| HTML + JS + Firebase SDK |
| 자동화         | Python 스크립트 기반 더미 생성기 |
| 문서화         | Markdown, Mermaid (ERD), PDF 보고서 |

## 7. 데이터 구조 요약

### 📘 MySQL

- `players`: player_id, name, rank, is_pro
- `matches`: match_id, black/white_player_id, result, rule, winrate, point_diff, etc.
- `moves`: match_id, move_number, x, y, color, time_taken

### 🔴 Firebase

```json
live_matches: {
  match_001: {
    players: { black, white },
    current_turn: 12,
    moves: {
      "1": {x, y, color, time_taken_sec},
      ...
    },
    last_updated: "timestamp"
  }
}
```

## 8. 예상 결과 및 시나리오

- 착점할 때마다 Firebase에 수 저장 + UI에 실시간 반영
- 대국 종료 시 Firebase → MySQL 결과 저장
- UI에서 과거 대국 목록과 진행 상황 열람 가능

## 9. 일정 (예시)

| 주차 | 목표 |
|------|------|
| 1주차 | 주제 선정 및 ERD 설계 완료 |
| 2주차 | MySQL 구현, Firebase 구조 설계 |
| 3주차 | 자동화 코드 작성 및 테스트 |
| 4주차 | UI 개발 및 연동 완료, 전체 통합 테스트 |

## 10. 마무리 계획

- `/MySQL/`, `/Firebase/`, `/Interface/`로 폴더 분리 정리
- 더미 데이터, ERD, UI 스크린샷 포함 `.zip` 제출
