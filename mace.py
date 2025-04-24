import serial
import struct
import time

def read_mace():
    try:
        port = "/dev/ttyAMA3"
        baudrate = 19200
        parity = serial.PARITY_NONE
        stopbits = serial.STOPBITS_ONE
        bytesize = serial.EIGHTBITS
        timeout = 1

        ser = serial.Serial(port, baudrate, bytesize, parity, stopbits, timeout)
        time.sleep(0.2) 
        request = bytearray([0x01, 0x04, 0x00, 0x00, 0x00, 0x06])
        crc = bytearray([0x70, 0x08])
        modbus_request = request + crc

        ser.write(modbus_request)
        time.sleep(0.2)  
        response = ser.read(256)

        if not response:
            print("No response received from MACE sensor")
            ser.close()
            return None, None, None
        
        if len(response) >= 15:  
            bat = round(struct.unpack('>f', response[3:7])[0], 2)
            depth = round(struct.unpack('>f', response[7:11])[0], 2)
            flow = round(struct.unpack('>f', response[11:15])[0], 2)
        else:
            print("Incomplete response received from MACE sensor")
            ser.close()
            return None, None, None

        ser.close()
        return bat, depth, flow
    except Exception as e:
        print(f"Error in read_modbus4: {e}")
        return None, None, None

def get_mace_data():
    return read_mace()
