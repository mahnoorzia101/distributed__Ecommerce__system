import mysql.connector
import os
import time

def get_conn():
    for i in range(10):
        try:
            # 1. Grab port from environment, convert to integer, default to 3306
            port_val = int(os.getenv("DB_PORT", 3306))
            
            return mysql.connector.connect(
                host=os.getenv("DB_HOST", "mysql"),
                port=port_val,                     # <-- Explicitly set custom port
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", "root"),
                database=os.getenv("DB_NAME"),
                ssl_disabled=False,                # <-- Enable SSL for Aiven Cloud
                ssl_verify_cert=False              # <-- Bypasses local CA certificate file validation
            )
        except Exception as e:
            print("Waiting for MySQL...", e)
            time.sleep(3)

    raise Exception("MySQL connection failed after retries")

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            password VARCHAR(100)
        )
    """)

    conn.commit()
    conn.close()