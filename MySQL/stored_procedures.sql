DELIMITER //

-- 플레이어 데이터 입력 프로시저
CREATE PROCEDURE InsertPlayer(
    IN p_name VARCHAR(100),
    IN p_rank VARCHAR(20),
    IN p_is_pro BOOLEAN
)
BEGIN
    INSERT INTO Player (name, rank, is_pro)
    VALUES (p_name, p_rank, p_is_pro);
END //

-- 대국 데이터 입력 프로시저
CREATE PROCEDURE InsertMatch(
    IN p_match_date DATE,
    IN p_rule VARCHAR(50),
    IN p_result VARCHAR(10),
    IN p_black_winrate FLOAT,
    IN p_point_difference INT,
    IN p_black_player_id INT,
    IN p_white_player_id INT
)
BEGIN
    INSERT INTO Match (match_date, rule, result, black_winrate, point_difference, 
                      black_player_id, white_player_id)
    VALUES (p_match_date, p_rule, p_result, p_black_winrate, p_point_difference,
            p_black_player_id, p_white_player_id);
END //

-- 수순 데이터 입력 프로시저
CREATE PROCEDURE InsertMove(
    IN p_match_id INT,
    IN p_move_number INT,
    IN p_color ENUM('B', 'W'),
    IN p_coordinate VARCHAR(10),
    IN p_time_elapsed INT
)
BEGIN
    INSERT INTO Move (match_id, move_number, color, coordinate, time_elapsed)
    VALUES (p_match_id, p_move_number, p_color, p_coordinate, p_time_elapsed);
END //

-- 플레이어 정보 조회 프로시저
CREATE PROCEDURE GetPlayer(
    IN p_player_id INT
)
BEGIN
    SELECT * FROM Player
    WHERE player_id = p_player_id;
END //

-- 대국 정보 조회 프로시저
CREATE PROCEDURE GetMatch(
    IN p_match_id INT
)
BEGIN
    SELECT m.*, 
           b.name as black_player_name,
           w.name as white_player_name
    FROM Match m
    JOIN Player b ON m.black_player_id = b.player_id
    JOIN Player w ON m.white_player_id = w.player_id
    WHERE m.match_id = p_match_id;
END //

-- 대국의 모든 수순 조회 프로시저
CREATE PROCEDURE GetMatchMoves(
    IN p_match_id INT
)
BEGIN
    SELECT * FROM Move
    WHERE match_id = p_match_id
    ORDER BY move_number;
END //

-- 플레이어 삭제 프로시저
CREATE PROCEDURE DeletePlayer(
    IN p_player_id INT
)
BEGIN
    DELETE FROM Player
    WHERE player_id = p_player_id;
END //

-- 대국 삭제 프로시저 (CASCADE로 인해 관련 수순도 자동 삭제됨)
CREATE PROCEDURE DeleteMatch(
    IN p_match_id INT
)
BEGIN
    DELETE FROM Match
    WHERE match_id = p_match_id;
END //

DELIMITER ;