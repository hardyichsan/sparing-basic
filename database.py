import psycopg2
from psycopg2 import sql
from datetime import datetime

DB_CONFIG = {
    "host": "localhost",
    "database": "wqms_db",
    "user": "postgres",
    "password": "has123456",
    "port": 5433
}

def insert_data(ph, orp, tds, conduct, do, salinity, nh3n, battery, depth, flow, tflow, turb, tss, cod, bod, no3, temp):
    query = """
    INSERT INTO sensor_datas (datetime, ph, orp, tds, conduct, diso, salinity, nh3n, battery, depth, flow, totalflow, turb, tss, cod, bod, no3, temp)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        timestamp = datetime.now()

        cursor.execute(query, (timestamp, ph, orp, tds, conduct, do, salinity, nh3n, battery, depth, flow, tflow, turb, tss, cod, bod, no3, temp))
        conn.commit()

        cursor.close()
        conn.close()
        print(f"[INFO] Data berhasil dimasukkan: {timestamp}, {ph}, {orp}, {tds}, {conduct}, {do}, {salinity}, {nh3n}, {battery}, {depth}, {flow}, {tflow}, {turb}, {tss}, {cod}, {bod}, {no3}, {temp}")
    except Exception as e:
        print(f"[ERROR] Gagal memasukkan data ke database: {e}")

