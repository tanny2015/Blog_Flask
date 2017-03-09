#coding=utf-8

from datetime import datetime
from flask import Flask, render_template
from flask_script import Manager
# (注意：注释和#之间 是要有一个空格的！)

from flask_bootstrap import Bootstrap
from flask_moment import Moment


app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)
# 之前写成moment = Moment() 导致一直出错，说是moment未定义！真是浪费了不少时间啊！
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manager.run()


# 实例3-13 加入一个datetime变量 时间显示 [3e]
# 测试URL1 404  http://127.0.0.1:5000





