import time
from at500 import get_at500_data
from mace import get_mace_data
from spectro import read_modbus_tcp
from database import insert_data
from datetime import datetime

# Ganti nilai interval sesuai kebutuhan (dalam menit)
interval = 1  # contoh: 1, 2, atau 3

try:
    while True:
        now = datetime.now()
        if now.minute % interval == 0 and now.second == 0:
            ph, tss, nh3n = get_at500_data()
            bat, depth, flow = get_mace_data()
            cod = read_modbus_tcp()

            print("\n=== SENSOR DATA ===")
            print(f"pH: {ph}, TSS: {tss}, NH3-N: {nh3n}")
            print(f"Bat: {bat}, Depth: {depth}, Flow: {flow}")
            print(f"COD: {cod} mg/L")
            print("===================")

            # Simpan data ke database
            insert_data(ph, tss, nh3n, depth, flow, cod)

            # Tunggu satu detik untuk menghindari pengulangan dalam satu menit
            time.sleep(1)
        else:
            # Cek lagi setiap detik
            time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram dihentikan oleh pengguna.")
