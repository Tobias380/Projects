import time 
import RPi.GPIO as gpio
from Adafruit_PWM_Servo_Driver import PWM

gpio.setmode (gpio.BOARD)
pwm = PWM(0x40, debug=True)
gpio.setup (7, gpio.OUT)
gpio.setup (12, gpio.OUT)

def Spin1 ():
  gpio.output(7, True)
  gpio.output(12, False)
  pwm.setPWMFreq(60)
  pwm.setPWM (0,0,2000) 
  time.sleep(2)
  
def Spin2 ():
  gpio.output(7, False)
  gpio.output(12, True)
  pwm.setPWMFreq(60)
  pwm.setPWM (0,0,2000) 
  time.sleep(2)
  
try:
  while (True):
    print 'Spin 1'
    Spin1 ()
    print 'Spin2'
    Spin2 ()
except KeyboardInterrupt :
  pwm.setPWM (0,0,0) 
  gpio.cleanup ()
    
  
