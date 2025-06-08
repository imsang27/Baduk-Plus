-- 플레이어 테이블
CREATE TABLE IF NOT EXISTS players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 게임 테이블
CREATE TABLE IF NOT EXISTS games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    black_player_id INT,
    white_player_id INT,
    game_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    black_score FLOAT,
    white_score FLOAT,
    winner ENUM('black', 'white', 'draw'),
    FOREIGN KEY (black_player_id) REFERENCES players(player_id),
    FOREIGN KEY (white_player_id) REFERENCES players(player_id)
);

-- 샘플 데이터 삽입
INSERT INTO players (player_name) VALUES 
('이세돌'),
('알파고'),
('신진서'),
('박정환');

-- 샘플 게임 데이터 삽입
INSERT INTO games (black_player_id, white_player_id, black_score, white_score, winner) VALUES
(1, 2, 3.5, 2.5, 'black'),
(3, 4, 4.5, 5.5, 'white'),
(2, 1, 6.5, 3.5, 'black'),
(4, 3, 2.5, 7.5, 'white'); 