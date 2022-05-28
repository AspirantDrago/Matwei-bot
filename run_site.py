from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def main():
    os.startfile('baza_dann.py')
    return 'Бот запущен!'


@app.route('/index')
def main():
    return 'Это бот Матвея!'


if __name__ == '__main__':
    port_run = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port_run)
