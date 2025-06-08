---
Date_of_creation: 2025-06-08 일 13:03:03
Last_modified:
  - 2025-06-08 일 16:56:25
aliases: 
tags: 
Reference: 
---
```sql title="저장 프로시저 예시"
DELIMITER $$

-- 입력: 수순 추가 프로시저
CREATE PROCEDURE AddMove(
  IN p_match_id VARCHAR(50),
  IN p_move_number INT,
  IN p_x INT,
  IN p_y INT,
  IN p_color VARCHAR(5),
  IN p_played_at DATETIME
)
BEGIN
  INSERT INTO moves (match_id, move_number, x, y, color, played_at)
  VALUES (p_match_id, p_move_number, p_x, p_y, p_color, p_played_at);
END$$

-- 조회: 대국 결과 조회 프로시저
CREATE PROCEDURE GetMatchResult(IN p_match_id VARCHAR(50))
BEGIN
  SELECT m.match_id, p1.name AS black_player, p2.name AS white_player,
         r.winner_color, r.reason, r.point_diff
  FROM matches m
  JOIN players p1 ON m.black_player_id = p1.player_id
  JOIN players p2 ON m.white_player_id = p2.player_id
  JOIN results r ON m.match_id = r.match_id
  WHERE m.match_id = p_match_id;
END$$

-- 삭제: 대국 및 수순 삭제 프로시저
CREATE PROCEDURE DeleteMatchData(IN p_match_id VARCHAR(50))
BEGIN
  DELETE FROM moves WHERE match_id = p_match_id;
  DELETE FROM results WHERE match_id = p_match_id;
  DELETE FROM matches WHERE match_id = p_match_id;
END$$

DELIMITER ;
```
