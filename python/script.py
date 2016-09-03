import webiopi
from webiopi.devices.serial import Serial

GPIO = webiopi.GPIO

RELAY1 = 26 # GPIO pin for RELAY1 using BCM numbering
RELAY2 = 19 # GPIO pin for RELAY2 using BCM numbering
RELAY3 = 13 # GPIO pin for RELAY3 using BCM numbering
RELAY4 = 6 # GPIO pin for RELAY4 using BCM numbering

port = Serial("ttyACM0", 9600)

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the relays to output
    GPIO.setFunction(RELAY1, GPIO.OUT)
    GPIO.setFunction(RELAY2, GPIO.OUT)
    GPIO.setFunction(RELAY3, GPIO.OUT)
    GPIO.setFunction(RELAY4, GPIO.OUT)
    GPIO.digitalWrite(RELAY1, GPIO.LOW)
    GPIO.digitalWrite(RELAY2, GPIO.LOW)
    GPIO.digitalWrite(RELAY3, GPIO.LOW)
    GPIO.digitalWrite(RELAY4, GPIO.LOW)

# loop function is repeatedly called by WebIOPi 
def loop():
    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(RELAY1, GPIO.LOW)
    GPIO.digitalWrite(RELAY2, GPIO.LOW)
    GPIO.digitalWrite(RELAY3, GPIO.LOW)
    GPIO.digitalWrite(RELAY4, GPIO.LOW)

# set the control mode
@webiopi.macro
def setMode(state):
    if(state == "1"):
        GPIO.digitalWrite(RELAY1, GPIO.LOW)
        GPIO.digitalWrite(RELAY2, GPIO.LOW)
        GPIO.digitalWrite(RELAY3, GPIO.LOW)
        GPIO.digitalWrite(RELAY4, GPIO.LOW)
        return "MODE 1 \n M1 = Tiller (UP/DOWN) \n M2 = Motor (LEFT/RIGHT)"
    elif (state == "2"):
        GPIO.digitalWrite(RELAY1, GPIO.LOW)
        GPIO.digitalWrite(RELAY2, GPIO.HIGH)
        GPIO.digitalWrite(RELAY3, GPIO.HIGH)
        GPIO.digitalWrite(RELAY4, GPIO.LOW)
        return "MODE 2 \n M1 = Hopper (UP/DOWN) \n M2 = Foot (LEFT/RIGHT)"
    else:
        GPIO.digitalWrite(RELAY1, GPIO.HIGH)
        GPIO.digitalWrite(RELAY2, GPIO.LOW)
        GPIO.digitalWrite(RELAY3, GPIO.LOW)
        GPIO.digitalWrite(RELAY4, GPIO.HIGH)
        return "MODE 3 \n M1 = Spike (UP/DOWN) \n M2 = Beak (LEFT/RIGHT)"

@webiopi.macro
def M1Forward():
    port.writeByte(0x61)
    return "Motor1 forward..."

@webiopi.macro
def M1Stop():
    port.writeByte(0x62)
    return "Motor1 stopped..."

@webiopi.macro
def M1Reverse():
    port.writeByte(0x63)
    return "Motor1 reverse..."
    
@webiopi.macro
def M2Forward():
    port.writeByte(0x64)
    return "Motor2 forward..."

@webiopi.macro
def M2Stop():
    port.writeByte(0x65)
    return "Motor2 stopped..."

@webiopi.macro
def M2Reverse():
    port.writeByte(0x66)
    return "Motor2 reverse..."
    
