import cv2
import datetime

# VideoCaptureオブジェクト取得
cap = cv2.VideoCapture(-1)

# 現在の日時を取得
current_datetime = datetime.datetime.now()
date_time_string = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")  # ファイル名に使用する日付と時間のフォーマットを設定

# 保存先のディレクトリとファイル名を指定
output_path = f'/home/ccuser/Desktop/avi/{date_time_string}_drive_recording.avi'

# ビデオの設定
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# ファイル名、エンコーディング方式、フレームレート、解像度を指定
width=1080
height=720
out = cv2.VideoWriter(output_path, fourcc,30.0, (width,height)) 

recording = False  # 録画中フラグ

print("start")

while True:
    # フレームを取得
    ret, frame = cap.read()

    if not ret:
        print("not capture")
        break

    # 画面サイズを指定
    frame = cv2.resize(frame, (width, height))

    # 取得したフレームをウィンドウ上に表示する
    cv2.imshow("frame", frame)

    # キーボード入力処理
    key = cv2.waitKey(1)
    if key == 13:  # Enterキーの場合録画開始または停止
        recording = not recording
        if recording:
            print("Recording started")
        else:
            print("Recording stopped")

    if recording:
        out.write(frame)  # フレームをビデオに追加

    if key == 27:  # Escキーの場合処理を抜ける
        break

# カメラデバイスクローズ
cap.release()

# ビデオライターを解放
out.release()

# ウィンドウクローズ
cv2.destroyAllWindows()
