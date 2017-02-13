#coding=utf-8

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


# 添加了动态的一些东西

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' %name


if __name__ == '__main__':
    app.run(debug=True)

# 测试URL :http://127.0.0.1:5000/user/tanny