---
Date_of_creation: 2025-06-08 일 12:47:22
Last_modified:
  - 2025-06-08 일 12:56:47
aliases: 
tags: 
Reference: 
---
```mermaid
erDiagram
    Player ||--o{ Match : participates_in
    Match ||--|{ Move : has
    Player {
        int player_id PK
        string name
        string rank
        boolean is_pro
    }
    Match {
        int match_id PK
        date match_date
        string rule
        string result
        float black_winrate
        int point_difference
        int black_player_id FK
        int white_player_id FK
    }
    Move {
        int move_id PK
        int match_id FK
        int move_number
        string color
        string coordinate
        int time_elapsed
    }
```
