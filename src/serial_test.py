import serial

ser = serial.Serial('COM3', 115200)

print("Listening for ESP32 data...\n")

while True:
    if ser.in_waiting:
        line = ser.readline().decode('utf-8').strip()
        print(line)