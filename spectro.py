import socket
import struct
import time

def read_modbus_tcp():
    print("Menghubungkan ke sensor Modbus TCP...")

    try:
        ip = "192.168.1.100"    # Ganti dengan IP sensor kamu
        port = 502
        unit_id = 0xFF          # Slave ID sensor
        start_address = 0x0092  # Alamat register untuk COD
        register_count = 2      # COD = 1 float = 2 register (16 bit)

        # Bangun request Modbus TCP (Function 04: Read Input Registers)
        transaction_id = 1
        protocol_id = 0x0000
        length = 6
        function_code = 0x04
        header = struct.pack('>HHHB', transaction_id, protocol_id, length, unit_id)
        body = struct.pack('>BHH', function_code, start_address, register_count)
        modbus_request = header + body

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((ip, port))
        sock.send(modbus_request)
        time.sleep(0.5)
        response = sock.recv(1024)
        sock.close()

        if not response or len(response) < 13:
            print("Response tidak valid.")
            return None

        cod_val = round(struct.unpack('>f', response[9:13])[0], 2)
        print(f"COD : {cod_val} mg/L")
        return cod_val

    except Exception as e:
        print(f"Terjadi error: {e}")
        return None
