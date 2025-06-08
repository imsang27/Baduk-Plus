DELIMITER //

-- 대국 결과 입력 프로시저
CREATE PROCEDURE InsertGameResult(
    IN p_game_id VARCHAR(255),
    IN p_result VARCHAR(50)
)
BEGIN
    INSERT INTO game_results (game_id, result)
    VALUES (p_game_id, p_result);
END //

-- 대국 결과 조회 프로시저
CREATE PROCEDURE GetGameResult(
    IN p_game_id VARCHAR(255)
)
BEGIN
    SELECT * FROM game_results
    WHERE game_id = p_game_id;
END //

-- 대국 결과 삭제 프로시저
CREATE PROCEDURE DeleteGameResult(
    IN p_game_id VARCHAR(255)
)
BEGIN
    DELETE FROM game_results
    WHERE game_id = p_game_id;
END //

DELIMITER ;