import serial
import time
import io
ser = serial.Serial('COM4', 115200, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
ser.close()
ser.open()
i, j = 0, 0

while 1: # i< 10:
    while j < 16:
        # ser.write(str(j).encode('utf-8'))
        a_bytes_big = j.to_bytes(2, 'little')
        ser.write(a_bytes_big)
        print(j)
        j += 1
        time.sleep(0.8)
    j = 0
    i += 1


ser.close()

