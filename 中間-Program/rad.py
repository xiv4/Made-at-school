import RPi.GPIO as GPIO
import time
 
assign_NUM = 23
 
def setup():
    #GPIO設定
    #GPIO番号を使う場合
    GPIO.setmode(GPIO.BCM) 
    #pin番号を使う場合
    #GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(assign_NUM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
 
def loop():
    while True:
        time.sleep(0.5)
        if (0 == GPIO.input(assign_NUM)):
            print("障害物を検知しました!!")
        
        else:
            print("Missing！")
 
 
def destroy():
    GPIO.cleanup()
 
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
