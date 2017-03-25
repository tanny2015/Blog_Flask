 #coding=utf-8
import os
from flask import Flask, render_template, session,  redirect, url_for
from flask_script import Manager,Shell
# (注意：注释和#之间 是要有一个空格的！)

from flask_bootstrap import Bootstrap
from flask_moment import Moment
# from flask_wtf import Form 这个已经过期了
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

manager = Manager(app)
bootstrap = Bootstrap(app)
# 之前写成moment = Moment() 导致一直出错，说是moment未定义！真是浪费了不少时间啊！
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Role(db.Model):
     __tablename__ = 'roles'
     id = db.Column(db.Integer,primary_key=True)
     name = db.Column(db.String(64),unique=True)
     users = db.relationship('User',backref='role', lazy='dynamic')

     def __repr__(self):
         return '<Role %r>'  % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %>' % self.name


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

def make_shell_context():
    return dict(app=app,db=db,User=User, Role=Role)
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500


@app.route('/', methods=['GET', 'POST'])
def index():
    # 这个是先新建一个输入表格，这个是自定义实现。具体实现在上边
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        # 如果这个名字之前没有收录，就把他添加到数据库
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        # 这个名字已经收录过，就不用再次收录
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'),
                           known=session.get('known',False))

if __name__ == '__main__':
    manager.run()




# 5.11.2 创建迁移脚本 数据库文件多出来一个version相关的表 [5d]
# 测试URL1 404  http://127.0.0.1:5000






































































