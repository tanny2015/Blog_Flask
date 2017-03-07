#coding=utf-8

from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)


if __name__ == '__main__':
    manager.run()


# 实例3-3 jinja2 hello.py 渲染模板 [3a]
# 注意这边一直报错是因为：你要把template那个文件夹去拷贝过来啊！！！
# 测试URL1 :http://127.0.0.1:5000
# 测试URL2 :http://127.0.0.1:5000/user/tanny