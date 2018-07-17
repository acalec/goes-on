import time

from models.task import Task
# from models import red
from . import ModelMixin
from . import db


class User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    avatar = db.Column(db.Text)
    followed = db.Column(db.Text)
    follower = db.Column(db.Text)
    status = db.Column(db.Integer)

    def __init__(self, form):
        self.role = form.get('role', 10)
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.followed = form.get('followed', 0)
        self.follower = form.get('follower', 0)
        self.status = form.get('status', 0)
        self.avatar = form.get('avatar', 'default')

    def _update(self, form):
        self.username = form.get('username', self.username)
        self.password = form.get('password', self.password)

    def get_avatar(self):
        if self.avatar == 'default':
            default_path = "/static/img/default.jpg"
            return default_path
        else:
            avatar_path = "/static/img/uploads/" + str(self.id) + "/" + str(self.avatar)
            return avatar_path

    def valid_username(self):
        if User.query.filter_by(username=self.username).first() is None:
            return True
        else:
            return False

    # 验证注册用户的合法性
    def valid(self):
        valid_username = self.valid_username()
        valid_username_len = len(self.username) >= 3
        valid_password_len = len(self.password) >= 3
        msgs = []
        if not valid_username:
            message = '用户名已经存在'
            msgs.append(message)
        if not valid_username_len:
            message = '用户名长度必须大于等于 3'
            msgs.append(message)
        if not valid_password_len:
            message = '密码长度必须大于等于 3'
            msgs.append(message)
        status = valid_username and valid_username_len and valid_password_len
        return status, msgs


def format_time(value):
    format = '%Y-%m-%d %H:%M'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt
