from flask import Flask, render_template, jsonify
import firebase_admin
from firebase_admin import credentials, db
import os

app = Flask(__name__)

# Firebase 초기화
cred = credentials.Certificate('./Firebase/firebase_auth.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv('FIREBASE_DB_URL')
})

# Firebase에서 게임 데이터 가져오기
def get_firebase_games():
    try:
        gibo_ref = db.reference('기보')
        games_data = gibo_ref.get()
        
        if not games_data:
            return []
            
        game_list = []
        
        for game_id, game_data in games_data.items():
            # 대국 결과 처리
            result = ""
            if '대국 결과' in game_data:
                result_data = game_data['대국 결과']
                winner = result_data.get('승자', '')
                win_type = result_data.get('승리_방식', '')
                score = result_data.get('집차이', '')
                moves = result_data.get('총수순', '')
                
                if winner and win_type:
                    result = f"{winner} {win_type}"
                    if score:
                        result += f" {score}"
                    if moves:
                        result += f" ({moves})"
            
            game_info = {
                'game_id': game_id,
                'tournament': game_data.get('기전명', ''),
                'black_player': game_data.get('대국자', {}).get('흑', {}).get('이름', ''),
                'white_player': game_data.get('대국자', {}).get('백', {}).get('이름', ''),
                'result': result
            }
            game_list.append(game_info)
            
        return game_list
    except Exception as e:
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/games', methods=['GET'])
def get_games():
    try:
        games = get_firebase_games()
        return jsonify(games)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 