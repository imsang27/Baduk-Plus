import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

def get_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            database=os.getenv('MYSQL_DATABASE'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD')
        )
        
        if connection.is_connected():
            print("MySQL 데이터베이스에 성공적으로 연결되었습니다.")
            return connection
            
    except Error as e:
        print(f"MySQL 연결 중 오류 발생: {e}")
        return None

def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("MySQL 연결이 종료되었습니다.") 