import psycopg2
from psycopg2 import sql
from datetime import datetime

# Konfigurasi koneksi database
DB_CONFIG = {
    "host": "localhost",
    "database": "wqms_db",
    "user": "postgres",
    "password": "has123456",
    "port": 5433
}

# Fungsi untuk menyimpan data ke database
def insert_data(total_rainfall, ph, tss, nh3n, depth, flow, cod):
    query = """
    INSERT INTO sensor_datas (datetime, rain, ph, tss, nh3n, depth, flow, cod)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        timestamp = datetime.now()

        cursor.execute(query, (timestamp, total_rainfall, ph, tss, nh3n, depth, flow, cod))
        conn.commit()

        cursor.close()
        conn.close()
        print(f"[INFO] Data berhasil dimasukkan: {timestamp}, {total_rainfall}, {ph}, {tss}, {nh3n}, {cod}, {depth}, {flow}")
    except Exception as e:
        print(f"[ERROR] Gagal memasukkan data ke database: {e}")
