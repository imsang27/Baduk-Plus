from flask import Flask, render_template, jsonify
import mysql.connector
from dotenv import load_dotenv
import os
import pandas as pd
import plotly.express as px
import json

app = Flask(__name__)

# 환경 변수 로드
load_dotenv()

# MySQL 연결 설정
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/statistics')
def get_statistics():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # 게임 통계 데이터 조회
    cursor.execute("""
        SELECT 
            DATE_FORMAT(game_date, '%Y-%m') as month,
            COUNT(*) as total_games,
            AVG(black_score) as avg_black_score,
            AVG(white_score) as avg_white_score
        FROM games
        GROUP BY DATE_FORMAT(game_date, '%Y-%m')
        ORDER BY month
    """)
    
    stats = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify(stats)

@app.route('/api/player-stats')
def get_player_stats():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # 플레이어 통계 데이터 조회
    cursor.execute("""
        SELECT 
            p.player_name,
            COUNT(g.game_id) as total_games,
            SUM(CASE WHEN g.winner = 'black' AND g.black_player_id = p.player_id 
                     OR g.winner = 'white' AND g.white_player_id = p.player_id 
                THEN 1 ELSE 0 END) as wins
        FROM players p
        LEFT JOIN games g ON p.player_id = g.black_player_id OR p.player_id = g.white_player_id
        GROUP BY p.player_id, p.player_name
    """)
    
    player_stats = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify(player_stats)

if __name__ == '__main__':
    app.run(debug=True) 