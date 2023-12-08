import time
from mpu6050 import mpu6050
import keyboard
import RPi.GPIO as GPIO
import requests

# MPU6050センサの初期化
sensor = mpu6050(0x68)

# GPIO設定
assign_NUM = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(assign_NUM, GPIO.IN, pull_up_down=GPIO.PUD_UP)

STR_NOTIFY_TOKEN = '[トークン番号]'
STR_NOTICE_MESSAGE = '鍵の忘れ物です！'

running = True

def exit_script(e):
    global running
    running = False

def send_line_notification(token, message):
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': message}
    response = requests.post(line_notify_api, headers=headers, data=data)
    if response.status_code == 200:
        print("LINE通知が送信されました")
    else:
        print(f"LINE通知の送信に失敗しました。ステータスコード: {response.status_code}")

def monitor_bike_movement():
    initial_accel_data = sensor.get_accel_data()
    threshold = 1.0

    keyboard.on_press_key("esc", exit_script)

    while running:
        accel_data = sensor.get_accel_data()

        x_accel = accel_data['x']
        y_accel = accel_data['y']
        z_accel = accel_data['z']

        x_diff = abs(x_accel - initial_accel_data['x'])
        y_diff = abs(y_accel - initial_accel_data['y'])
        z_diff = abs(z_accel - initial_accel_data['z'])

        if x_diff <= threshold and y_diff <= threshold and z_diff <= threshold:
            # 自転車が動いていない場合
            if GPIO.input(assign_NUM) == 0:
                print("自転車が動いていませんが、赤外線モジュールが検知されました")
                send_line_notification(STR_NOTIFY_TOKEN, STR_NOTICE_MESSAGE)

        if x_diff > threshold or y_diff > threshold or z_diff > threshold:
            print("自転車が動いています")

        initial_accel_data = accel_data

        time.sleep(1.0)

    keyboard.unhook_all()

def setup():
    pass

def loop():
    try:
        monitor_bike_movement()
    except KeyboardInterrupt:
        destroy()

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    loop()
