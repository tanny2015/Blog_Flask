#coding=utf-8

from flask import Flask, render_template
from flask_script import Manager
# (注意：注释和#之间 是要有一个空格的！)
from flask_bootstrap import Bootstrap

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('505.html'),500

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)


if __name__ == '__main__':
    manager.run()


# 实例3-9 使用模板继承机制简化页面模板 [3c]

# 测试URL1 404  http://127.0.0.1:5000/123
# 测试URL2 500  这个目前还不知道要怎么测试！

