-- 대국 정보 테이블
CREATE TABLE matches (
    match_id VARCHAR(255) PRIMARY KEY,
    black_player VARCHAR(100) NOT NULL,
    white_player VARCHAR(100) NOT NULL,
    black_rank VARCHAR(10),
    white_rank VARCHAR(10),
    match_date DATETIME NOT NULL,
    rules VARCHAR(50),
    result VARCHAR(50),
    score_diff FLOAT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 수순 기록 테이블
CREATE TABLE moves (
    move_id INT AUTO_INCREMENT PRIMARY KEY,
    match_id VARCHAR(255),
    move_number INT NOT NULL,
    color ENUM('black', 'white') NOT NULL,
    x_coord INT NOT NULL,
    y_coord INT NOT NULL,
    time_spent INT,  -- 초 단위
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (match_id) REFERENCES matches(match_id)
);