import board
import adafruit_lps35hw
import time

i2c = board.I2C()
lps = adafruit_lps35hw.LPS35HW(i2c)

lps.low_pass_enabled = True
while True:
   print("Pressure: %.2f hPa" % lps.pressure)
   print("")
   time.sleep(0.125)