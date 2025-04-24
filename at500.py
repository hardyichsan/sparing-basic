import serial
import struct
import time

# Jumlah maksimum percobaan jika tidak ada respon dari sensor
MAX_RETRIES = 3

def read_modbus(port, request, crc):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            baudrate = 19200
            parity = serial.PARITY_EVEN
            stopbits = serial.STOPBITS_ONE
            bytesize = serial.EIGHTBITS
            timeout = 1

            ser = serial.Serial(port, baudrate, bytesize, parity, stopbits, timeout)
            time.sleep(0.2)

            modbus_request = request + crc
            ser.write(modbus_request)
            time.sleep(0.2)  # Tunggu respons
            response = ser.read(256)

            if not response:
                print(f"Percobaan {attempt}/{MAX_RETRIES}: No response from {port}, retrying...")
                ser.close()
                time.sleep(0.5)  # Tunggu sebelum mencoba lagi
                continue

            if len(response) >= 7:  # Pastikan respons cukup panjang
                data = round(struct.unpack('>f', response[3:7])[0], 2)
                ser.close()
                return data
            else:
                print(f"Percobaan {attempt}/{MAX_RETRIES}: Incomplete response from {port}, retrying...")
                ser.close()
                time.sleep(0.5)
                continue

        except Exception as e:
            print(f"Percobaan {attempt}/{MAX_RETRIES}: Error reading Modbus: {e}, retrying...")
            time.sleep(0.5)  # Tunggu sebelum mencoba lagi

    print(f"Gagal membaca data dari {port} setelah {MAX_RETRIES} percobaan.")
    return None  # Kembalikan None jika gagal membaca setelah 3 percobaan

def read_ph():
    return read_modbus(
        "/dev/ttyAMA5",
        bytearray([0x01, 0x03, 0x15, 0xBA, 0x00, 0x02]),
        bytearray([0xE1, 0xE2])
    )

def read_tss():
    return read_modbus(
        "/dev/ttyAMA5",
        bytearray([0x01, 0x03, 0x16, 0x1C, 0x00, 0x02]),
        bytearray([0x01, 0x85])
    )

def read_nh3n():
    return read_modbus(
        "/dev/ttyAMA5",
        bytearray([0x01, 0x03, 0x16, 0x69, 0x00, 0x02]), #1657,1669
        bytearray([0x10, 0x5F])
    )

def get_at500_data():
    ph = read_ph()
    tss = read_tss()
    nh3n = read_nh3n()
    return ph, tss, nh3n

