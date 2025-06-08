import firebase_admin
from firebase_admin import credentials, firestore
from mysql_connection import get_mysql_connection, close_connection
import json
import time

# Firebase 초기화
cred = credentials.Certificate('firebase_auth.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def sync_firebase_to_mysql():
    """
    Firebase의 데이터를 MySQL로 동기화하는 함수
    """
    try:
        # MySQL 연결
        mysql_conn = get_mysql_connection()
        if not mysql_conn:
            return
        
        cursor = mysql_conn.cursor()
        
        # Firebase에서 데이터 가져오기
        users_ref = db.collection('users')
        users = users_ref.get()
        
        for user in users:
            user_data = user.to_dict()
            
            # MySQL에 데이터 삽입 또는 업데이트
            sql = """
                INSERT INTO users (user_id, name, email, created_at)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                name = VALUES(name),
                email = VALUES(email)
            """
            values = (
                user.id,
                user_data.get('name', ''),
                user_data.get('email', ''),
                user_data.get('created_at', None)
            )
            
            cursor.execute(sql, values)
        
        mysql_conn.commit()
        print("Firebase에서 MySQL로 데이터 동기화 완료")
        
    except Exception as e:
        print(f"동기화 중 오류 발생: {e}")
        
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'mysql_conn' in locals():
            close_connection(mysql_conn)

def sync_mysql_to_firebase():
    """
    MySQL의 데이터를 Firebase로 동기화하는 함수
    """
    try:
        # MySQL 연결
        mysql_conn = get_mysql_connection()
        if not mysql_conn:
            return
        
        cursor = mysql_conn.cursor(dictionary=True)
        
        # MySQL에서 데이터 가져오기
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        
        # Firebase에 데이터 업데이트
        for user in users:
            user_ref = db.collection('users').document(str(user['user_id']))
            user_ref.set({
                'name': user['name'],
                'email': user['email'],
                'created_at': user['created_at'].isoformat() if user['created_at'] else None
            })
        
        print("MySQL에서 Firebase로 데이터 동기화 완료")
        
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
            print(f'문서 변경 감지: {change.document.id}')
            sync_firebase_to_mysql()
        elif change.type.name == 'REMOVED':
            print(f'문서 삭제 감지: {change.document.id}')
            # 삭제된 문서 처리
            try:
                mysql_conn = get_mysql_connection()
                if mysql_conn:
                    cursor = mysql_conn.cursor()
                    cursor.execute("DELETE FROM users WHERE user_id = %s", (change.document.id,))
                    mysql_conn.commit()
                    cursor.close()
                    close_connection(mysql_conn)
                    print(f"MySQL에서 사용자 {change.document.id} 삭제 완료")
            except Exception as e:
                print(f"삭제 처리 중 오류 발생: {e}")

def start_realtime_sync():
    """
    Firebase 실시간 동기화 시작
    """
    print("Firebase 실시간 동기화 시작...")
    # users 컬렉션의 변경사항 감지
    users_ref = db.collection('users')
    users_ref.on_snapshot(on_snapshot)
    
    # 프로그램이 계속 실행되도록 유지
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n실시간 동기화를 종료합니다.")

if __name__ == "__main__":
    # 실시간 동기화 시작
    start_realtime_sync() 