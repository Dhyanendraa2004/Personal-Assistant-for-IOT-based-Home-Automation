import RPi.GPIO as GPIO
import time
import pyrebase
config = {
  "apiKey": "QFiGrPoHTkohHEjKzjsEIifbrzlR5BfTLfAd5t1V",
  "authDomain": "iothomeautmation.firebaseapp.com",
  "databaseURL": "https://iothomeautmation-default-rtdb.firebaseio.com",
  "storageBucket": "iothomeautmation.appspot.com"
}
f=False
firebase = pyrebase.initialize_app(config)
db = firebase.database()
print("Send Data to Firebase Using Raspberry Pi")
print("----------------------------------------")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ledRed = 17
ledGreen= 27
ledWhite = 22
fannn = 19
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledWhite, GPIO.OUT)
GPIO.setup(fannn, GPIO.OUT)
GPIO.setup(fannn,GPIO.OUT)
GPIO.output(ledWhite, GPIO.LOW)
GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledGreen, GPIO.LOW)
GPIO.setup(18,GPIO.OUT)

servo = GPIO.PWM(18,100)
servo.start(0)
time.sleep(1)
x=0

def read_temperature():
    reading = GPIO.input(23)
    voltage = reading * 3.3  # Assuming 3.3V input
    temperature_c = voltage * 100  # Each 10mV corresponds to 1 degree Celsius
    return temperature_c

#pwm=GPIO.PWM(3, 50)
#pwm.start(0)

while True:
    temperature = read_temperature()
    print("Temperature: {:.2f} °C".format(temperature))
    time.sleep(1)
    myData = db.child("finalapp").get().val()
    door = myData["door"]
    redl = myData["redl"]
    green = myData["whtl2"]
    whtl = myData["whtl"]
    fan = myData["fan1"]
    redl = myData["redl"]
    redl = myData["redl"]
    autoo = 0
    #myData["autoo"]
    voic = myData["voic"]
    if voic == '1':
        str=myData["str"]
        command = str
        #red light
        if "on" in command and "red" in command:
            device_name = "Red Light"
            print(f"Turning on {device_name}")
            GPIO.output(ledRed,GPIO.HIGH)
        elif "off" in command and "red" in command:
            device_name = "Red Light"
            print(f"Turning off {device_name}")
            GPIO.output(ledRed,GPIO.LOW)
        #white light
        elif "on" in command and "white" in command:
            device_name = "White Light"
            print(f"Turning off {device_name}")
            GPIO.output(ledWhite,GPIO.HIGH)
        elif "off" in command and "white" in command:
            device_name = "White Light"
            print(f"Turning off {device_name}")
            GPIO.output(ledWhite,GPIO.LOW)
        #green light
        elif "on" in command and "green" in command:
            device_name = "Green Light"
            print(f"Turning off {device_name}")
            GPIO.output(ledGreen,GPIO.HIGH)
        elif "off" in command and "green" in command:
            device_name = "Green Light"
            print(f"Turning off {device_name}")
            GPIO.output(ledGreen,GPIO.LOW)
        #Fan
        elif "on" in command and "fan" in command:
            device_name = "Fan"
            print(f"Turning off {device_name}")
            GPIO.output(fannn,GPIO.HIGH)
        elif "off" in command and "fan" in command:
            device_name = "Fan"
            print(f"Turning off {device_name}")
            GPIO.output(fannn,GPIO.LOW)
        
        #Door               
        if "open" in command and "door" in command:
            device_name = "Door"
            print(f"Opening the {device_name}")
            x=1
            print ("Rotating at intervals of 90 degrees")
            duty = 2
            while duty <= 13:
                servo.ChangeDutyCycle(duty)
                if(duty!=2):
                        time.sleep(1)
                duty = duty + 10
                time.sleep(1)
            f=True
        elif "close" in command and "door" in command:
            device_name = "Door"
            print(f"Closing the {device_name}")
            f=False
            x=0
            print ("Turning back to 0 degrees")
            servo.ChangeDutyCycle(2)                    
            time.sleep(1)
            servo.ChangeDutyCycle(0)
        else:
            print("Invalid command or device name not found.")  
    else:
        if autoo=='1':
            ...
        else:
            #redl light
            if redl == '1':
               GPIO.output(ledRed,GPIO.HIGH)
            elif redl == '0':
               GPIO.output(ledRed,GPIO.LOW)
        
            #white light1
            if whtl == '1':
               GPIO.output(ledWhite,GPIO.HIGH)
            elif whtl == '0':
               GPIO.output(ledWhite,GPIO.LOW)
        
            #white light 2
            if green == '1':
               GPIO.output(ledGreen,GPIO.HIGH)
            elif green == '0':
               GPIO.output(ledGreen,GPIO.LOW)
        
            #fan
            if fan == '1':
               GPIO.output(fannn,GPIO.HIGH)
            elif fan == '0':
               GPIO.output(fannn,GPIO.LOW)
            
            #door
            if door == '1' and f==False:
                x=1
                print ("Rotating at intervals of 90 degrees")
                duty = 2
                while duty <= 13:
                    servo.ChangeDutyCycle(duty)
                    if(duty!=2):
                            time.sleep(1)
                    duty = duty + 10
                    time.sleep(1)
                f=True
            elif door == '0':
                f=False
                x=0
                print ("Turning back to 0 degrees")
                servo.ChangeDutyCycle(2)                    
                time.sleep(1)
                servo.ChangeDutyCycle(0)


    