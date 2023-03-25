import Jetson.GPIO as GPIO
import time, serial
GPIO.setmode(GPIO.BOARD) 

class Wheels():
    def __init__(self):
        print("----------Wheels are ready----------")
        #FL:
        self.FL_IN1=7
        self.FL_IN2=11

        #FR:
        self.FR_IN1=12
        self.FR_IN2=15

        #BF:
        self.BL_IN1=19
        self.BL_IN2=21

        #BR:
        self.BR_IN1=26
        self.BR_IN2=23

        #Initialize FL_ENA, self.FL_IN1, and self.FL_IN2
        
        GPIO.setup(self.FL_IN1,GPIO.OUT)
        GPIO.setup(self.FL_IN2,GPIO.OUT)

       #Initialize FR_ENA, self.FR_IN1, and self.FR_IN2
        
        GPIO.setup(self.FR_IN1,GPIO.OUT)
        GPIO.setup(self.FR_IN2,GPIO.OUT)

        #Initialize BL_ENA, self.BL_IN1, and self.BL_IN2
        
        GPIO.setup(self.BL_IN1,GPIO.OUT)
        GPIO.setup(self.BL_IN2,GPIO.OUT)

        #Initialize BR_ENA, self.BR_IN1, and self.BR_IN2
        
        GPIO.setup(self.BR_IN1,GPIO.OUT)
        GPIO.setup(self.BR_IN2,GPIO.OUT)
        
    def stop(self):
        # FL_Stop
        GPIO.output(self.FL_IN1, GPIO.LOW)
        GPIO.output(self.FL_IN2, GPIO.LOW)

        # FR_Stop
        GPIO.output(self.FR_IN1, GPIO.LOW)
        GPIO.output(self.FR_IN2, GPIO.LOW)

        # BL_Stop
        GPIO.output(self.BL_IN1, GPIO.LOW)
        GPIO.output(self.BL_IN2, GPIO.LOW)

        # BR_Stop
        GPIO.output(self.BR_IN1, GPIO.LOW)
        GPIO.output(self.BR_IN2, GPIO.LOW)
        
    def forward(self):
        while True:
            try:
                # FL_Forward
                GPIO.output(self.FL_IN1, GPIO.HIGH)
                GPIO.output(self.FL_IN2, GPIO.LOW)

                # FR_Forward
                GPIO.output(self.FR_IN1, GPIO.HIGH)
                GPIO.output(self.FR_IN2, GPIO.LOW)

                # BL_Forward
                GPIO.output(self.BL_IN1, GPIO.HIGH)
                GPIO.output(self.BL_IN2, GPIO.LOW)

                # BR_Forward
                GPIO.output(self.BR_IN1, GPIO.HIGH)
                GPIO.output(self.BR_IN2, GPIO.LOW)
            except:
                self.stop()
                
    def backward(self):
        while True:
            try:
                GPIO.output(self.FL_IN1, GPIO.LOW)
                GPIO.output(self.FL_IN2, GPIO.HIGH)

                # FR_Revese
                GPIO.output(self.FR_IN1, GPIO.LOW)
                GPIO.output(self.FR_IN2, GPIO.HIGH)

                # BL_Revese
                GPIO.output(self.BL_IN1, GPIO.LOW)
                GPIO.output(self.BL_IN2, GPIO.HIGH)

                # BR_Revese
                GPIO.output(self.BR_IN1, GPIO.LOW)
                GPIO.output(self.BR_IN2, GPIO.HIGH)
            except:
                self.stop()
        
    def left(self):
        while True:
            try:
                # FL_Left
                GPIO.output(self.FL_IN1, GPIO.LOW)
                GPIO.output(self.FL_IN2, GPIO.HIGH)

                # FR_Left
                GPIO.output(self.FR_IN1, GPIO.HIGH)
                GPIO.output(self.FR_IN2, GPIO.LOW)

                # BL_Left
                GPIO.output(self.BL_IN1, GPIO.HIGH)
                GPIO.output(self.BL_IN2, GPIO.LOW)

                # BR_Left
                GPIO.output(self.BR_IN1, GPIO.LOW)
                GPIO.output(self.BR_IN2, GPIO.HIGH)
            except:
                self.stop()
                
    def right(self):
        while True:
            try:
                # FL_Right
                GPIO.output(self.FL_IN1, GPIO.HIGH)
                GPIO.output(self.FL_IN2, GPIO.LOW)

                # FR_Right
                GPIO.output(self.FR_IN1, GPIO.LOW)
                GPIO.output(self.FR_IN2, GPIO.HIGH)

                # BL_Right
                GPIO.output(self.BL_IN1, GPIO.LOW)
                GPIO.output(self.BL_IN2, GPIO.HIGH)

                # BR_Right
                GPIO.output(self.BR_IN1, GPIO.HIGH)
                GPIO.output(self.BR_IN2, GPIO.LOW)
            except:
                self.stop()
        
    def ccw(self):
        while True:
            try:
                # FL_CCW
                GPIO.output(self.FL_IN1, GPIO.LOW)
                GPIO.output(self.FL_IN2, GPIO.HIGH)

                # FR_CCW
                GPIO.output(self.FR_IN1, GPIO.HIGH)
                GPIO.output(self.FR_IN2, GPIO.LOW)

                # BL_CCW
                GPIO.output(self.BL_IN1, GPIO.LOW)
                GPIO.output(self.BL_IN2, GPIO.HIGH)

                # BR_CCW
                GPIO.output(self.BR_IN1, GPIO.HIGH)
                GPIO.output(self.BR_IN2, GPIO.LOW)
            except:
                self.stop()
                
    def cw(self):
            while True:
                try:
                    # FL_CW
                    GPIO.output(self.FL_IN1, GPIO.HIGH)
                    GPIO.output(self.FL_IN2, GPIO.LOW)

                    # FR_CW
                    GPIO.output(self.FR_IN1, GPIO.LOW)
                    GPIO.output(self.FR_IN2, GPIO.HIGH)

                    # BL_CW
                    GPIO.output(self.BL_IN1, GPIO.HIGH)
                    GPIO.output(self.BL_IN2, GPIO.LOW)

                    # BR_CW
                    GPIO.output(self.BR_IN1, GPIO.LOW)
                    GPIO.output(self.BR_IN2, GPIO.HIGH)
                except:
                    self.stop()
          
    def cleanup(self):
        GPIO.cleanup()
        print('clean up')
        
    
    # if you want to call out an object/ a function in a class, 
    # syntax should be class().object()
    # for example Wheels().forward(), Wheels().backward(), etc..
    # for remote control, 
    # if key=="down arrow":  # (i dont know the syntax of down arrow key)
    #   try:
    #       print('backward')
    #       Wheels().backward()
    #   except: /or except +name of error that Python returns:
    #       print('stop')
    #        Wheels().stop()
