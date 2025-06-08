import firebase_admin
from firebase_admin import credentials, db
import sys
import os
from dotenv import load_dotenv

# 상위 디렉토리를 Python 경로에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from MySQL.mysql_connection import get_mysql_connection, close_connection
import json
import time

load_dotenv()
FIREBASE_DB_URL = os.getenv("FIREBASE_DB_URL")

# Firebase 초기화
cred = credentials.Certificate('./Firebase/firebase_auth.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': FIREBASE_DB_URL
    })

def sync_firebase_to_mysql():
    """
    Firebase의 대국 결과를 MySQL로 동기화하는 함수
    """
    try:
        print("MySQL 연결 시도...")
        # MySQL 연결
        mysql_conn = get_mysql_connection()
        if not mysql_conn:
            print("MySQL 연결 실패")
            return
        
        cursor = mysql_conn.cursor()
        print("MySQL 연결 성공")
        
        # Firebase에서 기보 데이터 가져오기
        print("Firebase에서 데이터 가져오기 시도...")
        gibos_ref = db.reference('기보')
        gibos = gibos_ref.get()
        
        if gibos:
            print(f"Firebase에서 {len(gibos)}개의 기보 데이터를 가져왔습니다.")
            for game_id, gibo_data in gibos.items():
                print(f"기보 {game_id} 처리 중...")
                # 대국 결과가 있는 경우에만 처리
                if '대국 결과' in gibo_data:
                    sql = """
                        INSERT INTO game_results (game_id, result)
                        VALUES (%s, %s)
                        ON DUPLICATE KEY UPDATE
                            result = VALUES(result)
                    """
                    result = json.dumps(gibo_data['대국 결과'], ensure_ascii=False)
                    values = (game_id, result)
                    
                    try:
                        cursor.execute(sql, values)
                        print(f"대국 결과 동기화 성공: {game_id} - {result}")
                    except Exception as e:
                        print(f"SQL 실행 중 오류 발생: {e}")
        else:
            print("Firebase에서 가져온 데이터가 없습니다.")
        
        mysql_conn.commit()
        print("Firebase에서 MySQL로 대국 결과 동기화 완료")
        
    except Exception as e:
        print(f"동기화 중 오류 발생: {e}")
        
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'mysql_conn' in locals():
            close_connection(mysql_conn)

def on_value_change(event):
    """
    Firebase 데이터 변경을 감지하는 콜백 함수
    """
    print(f'데이터 변경 감지: {event.path}')
    sync_firebase_to_mysql()

def start_realtime_sync():
    """
    Firebase 실시간 동기화 시작
    """
    print("Firebase 실시간 동기화 시작...")
    
    # 기보 데이터의 변경사항 감지
    gibos_ref = db.reference('기보')
    gibos_ref.listen(on_value_change)
    print("기보 데이터 리스너 설정 완료")
    
    # 프로그램이 계속 실행되도록 유지
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n실시간 동기화를 종료합니다.")

if __name__ == "__main__":
    # 실시간 동기화 시작
    start_realtime_sync() 