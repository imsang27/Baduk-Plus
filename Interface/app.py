from flask import Flask, render_template, jsonify, request, redirect, url_for
import mysql.connector
from dotenv import load_dotenv
import os
import pandas as pd
import plotly.express as px
import json
import logging

# 로깅 설정
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# 환경 변수 로드
load_dotenv()

# MySQL 연결 설정
def get_db_connection():
    try:
        # 환경 변수 값 로깅
        logger.debug(f"DB Connection Settings:")
        logger.debug(f"Host: {os.getenv('MYSQL_HOST')}")
        logger.debug(f"Database: {os.getenv('MYSQL_DATABASE')}")
        logger.debug(f"User: {os.getenv('MYSQL_USER')}")
        logger.debug(f"Password: {'*' * len(os.getenv('MYSQL_PASSWORD', ''))}")
        
        return mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            database=os.getenv('MYSQL_DATABASE'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
        )
    except Exception as e:
        logger.error(f"Database connection error: {str(e)}")
        raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/statistics')
def get_statistics():
    try:
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
    except Exception as e:
        logger.error(f"Statistics API error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/player-stats')
def get_player_stats():
    try:
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
    except Exception as e:
        logger.error(f"Player stats API error: {str(e)}")
        return jsonify({"error": str(e)}), 500

# 플레이어 관련 API
@app.route('/api/players', methods=['GET'])
def get_players():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM players ORDER BY player_name")
        players = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(players)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/players', methods=['POST'])
def add_player():
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO players (player_name) VALUES (%s)",
            (data['player_name'],)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "플레이어가 추가되었습니다."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/players/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM players WHERE player_id = %s", (player_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "플레이어가 삭제되었습니다."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 게임 관련 API
@app.route('/api/games', methods=['GET'])
def get_games():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT g.*, 
                   b.player_name as black_player_name,
                   w.player_name as white_player_name
            FROM games g
            JOIN players b ON g.black_player_id = b.player_id
            JOIN players w ON g.white_player_id = w.player_id
            ORDER BY g.game_date DESC
        """)
        games = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(games)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/games', methods=['POST'])
def add_game():
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO games 
            (black_player_id, white_player_id, black_score, white_score, winner)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            data['black_player_id'],
            data['white_player_id'],
            data['black_score'],
            data['white_score'],
            data['winner']
        ))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "게임이 추가되었습니다."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM games WHERE game_id = %s", (game_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "게임이 삭제되었습니다."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 