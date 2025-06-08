DELIMITER //

-- 데이터 입력을 위한 저장 프로시저
CREATE PROCEDURE InsertData(
    IN p_name VARCHAR(100),
    IN p_description TEXT
)
BEGIN
    INSERT INTO your_table_name (name, description, created_at)
    VALUES (p_name, p_description, NOW());
END //

-- 데이터 조회를 위한 저장 프로시저
CREATE PROCEDURE GetData(
    IN p_id INT
)
BEGIN
    SELECT * FROM your_table_name
    WHERE id = p_id;
END //

-- 모든 데이터 조회를 위한 저장 프로시저
CREATE PROCEDURE GetAllData()
BEGIN
    SELECT * FROM your_table_name
    ORDER BY created_at DESC;
END //

-- 데이터 삭제를 위한 저장 프로시저
CREATE PROCEDURE DeleteData(
    IN p_id INT
)
BEGIN
    DELETE FROM your_table_name
    WHERE id = p_id;
END //

DELIMITER ; 