import time
from mpu6050 import mpu6050
import keyboard

def exit_script():
    global running
    running = False

def monitor_bike_movement():
    sensor = mpu6050(0x68)
    initial_accel_data = sensor.get_accel_data()
    threshold = 1.0
    global running
    running = True

    # キーボードイベントハンドラを追加
    keyboard.add_hotkey("ctrl+c", exit_script)

    try:
        while running:
            accel_data = sensor.get_accel_data()

            x_accel = accel_data['x']
            y_accel = accel_data['y']
            z_accel = accel_data['z']

            x_diff = abs(x_accel - initial_accel_data['x'])
            y_diff = abs(y_accel - initial_accel_data['y'])
            z_diff = abs(z_accel - initial_accel_data['z'])

            if x_diff > threshold or y_diff > threshold or z_diff > threshold:
                print("自転車が動いています")

            initial_accel_data = accel_data

            time.sleep(1.0)
    except KeyboardInterrupt:
        pass  # Ctrl+Cが押されたときに例外をキャッチして終了します

    keyboard.unhook_all()

if __name__ == "__main__":
    monitor_bike_movement()
