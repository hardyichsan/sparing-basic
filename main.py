import time
from at500 import get_at500_data
from mace import get_mace_data
from rain import get_rainfall, cleanup
from spectro import read_modbus_tcp
from database import insert_data

try:
    while True:
        tipping_count, total_rainfall = get_rainfall()
        ph, tss, nh3n = get_at500_data()
        bat, depth, flow = get_mace_data()
        cod = read_modbus_tcp()

        print("\n=== SENSOR DATA ===")
        print(f"Jumlah tipping: {tipping_count}")
        print(f"Total curah hujan: {total_rainfall:.3f} mm")
        print(f"pH: {ph}, TSS: {tss}, NH3-N: {nh3n}")
        print(f"Bat: {bat}, Depth: {depth}, Flow: {flow}")
        print(f"COD: {cod} mg/L")
        print("===================")

        # Simpan data ke database
        insert_data(total_rainfall, ph, tss, nh3n, depth, flow, cod)

        time.sleep(2)

except KeyboardInterrupt:
    print("\nProgram dihentikan oleh pengguna.")
finally:
    cleanup()
