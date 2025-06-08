-- 대국 결과 테이블
CREATE TABLE game_results (
    game_id VARCHAR(255) PRIMARY KEY,
    result VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);