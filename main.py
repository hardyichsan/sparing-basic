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
            ph, orp, tds, conduct, do, salinity, nh3n = get_at500_data()
            battery, depth, flow, tflow = get_mace_data()
            turb, tss, cod, bod, no3, temp = read_modbus_tcp()

            print("\n=== SENSOR DATA ===")
            print(f"pH: {ph}, ORP: {orp}, TDS: {tds}, Conductivity: {conduct}, DO: {do}, Salinity: {salinity}, NH3-N: {nh3n}")
            print(f"Bat: {battery}, Depth: {depth}, Flow: {flow}, TFlow: {tflow}")
            print(f"Turbidity: {turb}, TSS: {tss}, COD: {cod}, BOD: {bod}, NO3: {no3}, Temp: {temp}")
            print("===================")

            # Simpan data ke database
            insert_data(ph, orp, tds, conduct, do, salinity, nh3n, battery, depth, flow, tflow, turb, tss, cod, bod, no3, temp)
            print("Data berhasil disimpan ke database.")

            # Tunggu satu detik untuk menghindari pengulangan dalam satu menit
            time.sleep(1)
        else:
            # Cek lagi setiap detik
            time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram dihentikan oleh pengguna.")
