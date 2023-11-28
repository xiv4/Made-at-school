import RPi.GPIO as GPIO
import tkinter as tk

# GPIOピンの設定
buzzer_pin = 10  # ブザーを接続したGPIOピン番号

# GPIOの初期化
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

# ブザーの状態を管理する変数
buzzer_on = False

# ブザーを鳴らす関数
def toggle_buzzer():
    global buzzer_on
    if buzzer_on:
        GPIO.output(buzzer_pin, GPIO.HIGH)
    else:
        GPIO.output(buzzer_pin, GPIO.LOW)
    buzzer_on = not buzzer_on

# Tkinterウィンドウの作成
root = tk.Tk()
root.title("Buzzer Control")

# ボタンを配置
button = tk.Button(root, text="Toggle Buzzer", command=toggle_buzzer)
button.pack()

# アプリケーションの実行
root.mainloop()

# アプリケーションが終了した後にGPIOのクリーンアップ
GPIO.cleanup()
