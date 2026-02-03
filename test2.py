import serial
import time
ser = serial.Serial("COM3", 9600)

a = 0
rcoff = 1
gcoff = 0.1
bcoff = 0.2

coffs = [rcoff, gcoff, bcoff]

rgb = [0, 0, 0]

while True:

    for c in range(0, 3):
        rgb[c] = round(a * coffs[c])
    
    print([0x01, 0x03, rgb[0], rgb[1], rgb[2], rgb[0] ^ rgb[1] ^ rgb[2]])
    ser.write(bytes([0x01, 0x03, rgb[0], rgb[1], rgb[2], rgb[0] ^ rgb[1] ^ rgb[2]]))
    ser.reset_input_buffer()
    
    a += 1
    a = a % 255

    time.sleep(0.05)
