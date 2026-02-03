import serial
import time
ser = serial.Serial("COM3", 9600)

a = 100
rcoff = 1
gcoff = 0.1
bcoff = 0.1

while True:
    
    r = chr(round(a * rcoff))
    g = chr(round(a * gcoff))
    b = chr(round(a * bcoff))
    # a += 1
    # a = a % 255
    time.sleep(0.05)
    ser.write((str(r) + str(g) + str(b) + str('\n')).encode())
    print(f"{ord(r):3} {ord(g):3} {ord(b):3}")
    ser.reset_input_buffer()
