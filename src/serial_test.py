import serial

ser = serial.Serial('COM3', 115200)

print("Listening for ESP32 data...")

while True:
    line = ser.readline().decode('utf-8', errors='ignore').strip()
    
    if line:
        print(line)