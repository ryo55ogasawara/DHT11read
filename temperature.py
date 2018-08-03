import dht11
import RPi.GPIO as GPIO
import time
from datetime import datetime
 
# Define GPIO to LCD mapping
Temp_sensor=4
  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
instance = dht11.DHT11(pin = Temp_sensor)
   
while True:
    #get DHT11 sensor value
    result = instance.read()
    if result.is_valid():
        #print("temp:"+str(result.temperature)+" C")
        #print("humid:"+str(result.humidity)+"%")
        print(datetime.now().strftime("%Y/%m/%d %H:%M:%S")+", temp:"+str(result.temperature)+" C, humid:"+str(result.humidity)+"%")
        time.sleep(3) # 3 second delay

