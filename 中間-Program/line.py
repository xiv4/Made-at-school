import requests

STR_NOTIFY_TOKEN = '[APIコード]'
STR_NOTICE_MESSAGE = 'LINEへのメッセージ'

def send_line_notification(token, message):
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': message}
    response = requests.post(line_notify_api, headers=headers, data=data)
    if response.status_code == 200:
        print("LINE通知が送信されました")
    else:
        print(f"LINE通知の送信に失敗しました。ステータスコード: {response.status_code}")

# メインプログラム
if __name__ == "__main__":
    send_line_notification(STR_NOTIFY_TOKEN, STR_NOTICE_MESSAGE)
