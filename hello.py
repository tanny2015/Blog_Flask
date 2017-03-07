#coding=utf-8

from flask import Flask, render_template
from flask_script import Manager
# 新增(注意：注释和#之间 是要有一个空格的！)

from flask_bootstrap import Bootstrap

app = Flask(__name__)

manager = Manager(app)
# 新增
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)


if __name__ == '__main__':
    manager.run()


# 实例3-5 使用Flask-Bootstrap的模板 [3b]

# 测试URL1 :http://127.0.0.1:5000
# 测试URL2 :http://127.0.0.1:5000/user/tanny