import firebase_admin
from firebase_admin import credentials, firestore
from MySQL.mysql_connection import get_mysql_connection, close_connection
import json
import time

# Firebase 초기화
cred = credentials.Certificate('firebase_auth.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def sync_firebase_to_mysql():
    """
    Firebase의 대국 결과를 MySQL로 동기화하는 함수
    """
    try:
        # MySQL 연결
        mysql_conn = get_mysql_connection()
        if not mysql_conn:
            return
        
        cursor = mysql_conn.cursor()
        
        # Firebase에서 대국 데이터 가져오기
        games_ref = db.collection('games')
        games = games_ref.get()
        
        for game in games:
            game_data = game.to_dict()
            
            # 대국 결과만 MySQL에 저장
            if '대국 결과' in game_data:
                sql = """
                    INSERT INTO game_results (game_id, result)
                    VALUES (%s, %s)
                    ON DUPLICATE KEY UPDATE
                    result = VALUES(result)
                """
                values = (
                    game.id,
                    game_data['대국 결과']
                )
                
                cursor.execute(sql, values)
        
        mysql_conn.commit()
        print("Firebase에서 MySQL로 대국 결과 동기화 완료")
        
    except Exception as e:
        print(f"동기화 중 오류 발생: {e}")
        
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'mysql_conn' in locals():
            close_connection(mysql_conn)

def on_snapshot(doc_snapshot, changes, read_time):
    """
    Firebase 문서 변경을 감지하는 콜백 함수
    """
    for change in changes:
        if change.type.name == 'ADDED' or change.type.name == 'MODIFIED':
            print(f'대국 결과 변경 감지: {change.document.id}')
            sync_firebase_to_mysql()
        elif change.type.name == 'REMOVED':
            print(f'대국 결과 삭제 감지: {change.document.id}')
            # 삭제된 대국 결과 처리
            try:
                mysql_conn = get_mysql_connection()
                if mysql_conn:
                    cursor = mysql_conn.cursor()
                    cursor.execute("DELETE FROM game_results WHERE game_id = %s", (change.document.id,))
                    mysql_conn.commit()
                    cursor.close()
                    close_connection(mysql_conn)
                    print(f"MySQL에서 대국 결과 {change.document.id} 삭제 완료")
            except Exception as e:
                print(f"삭제 처리 중 오류 발생: {e}")

def start_realtime_sync():
    """
    Firebase 실시간 동기화 시작
    """
    print("Firebase 실시간 동기화 시작...")
    # games 컬렉션의 변경사항 감지
    games_ref = db.collection('games')
    games_ref.on_snapshot(on_snapshot)
    
    # 프로그램이 계속 실행되도록 유지
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n실시간 동기화를 종료합니다.")

if __name__ == "__main__":
    # 실시간 동기화 시작
    start_realtime_sync() 