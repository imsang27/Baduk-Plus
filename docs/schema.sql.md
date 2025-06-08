---
Date_of_creation: 2025-06-08 일 12:58:16
Last_modified:
  - 2025-06-08 일 12:59:03
aliases: 
tags: 
Reference: 
---
```sql
-- 플레이어 테이블
CREATE TABLE Player (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    rank VARCHAR(20),
    is_pro BOOLEAN DEFAULT FALSE
);

-- 대국 테이블
CREATE TABLE Match (
    match_id INT AUTO_INCREMENT PRIMARY KEY,
    match_date DATE NOT NULL,
    rule VARCHAR(50),
    result VARCHAR(10),
    black_winrate FLOAT,
    point_difference INT,
    black_player_id INT NOT NULL,
    white_player_id INT NOT NULL,
    FOREIGN KEY (black_player_id) REFERENCES Player(player_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (white_player_id) REFERENCES Player(player_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- 수순 테이블
CREATE TABLE Move (
    move_id INT AUTO_INCREMENT PRIMARY KEY,
    match_id INT NOT NULL,
    move_number INT NOT NULL,
    color ENUM('B', 'W') NOT NULL,
    coordinate VARCHAR(10) NOT NULL,
    time_elapsed INT,
    FOREIGN KEY (match_id) REFERENCES Match(match_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
```