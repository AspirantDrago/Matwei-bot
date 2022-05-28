from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def start_bot_page():
    import main
    return 'Бот запущен!'


@app.route('/index')
def info_page():
    return 'Это бот Матвея!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
