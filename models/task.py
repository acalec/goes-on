import json
from . import *


class Task(db.Model, ModelMixin):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    content = db.Column(db.String())
    created_time = db.Column(db.Integer)
    updated_time = db.Column(db.Integer)
    paused = db.Column(db.String())
    status = db.Column(db.String())
    status_list = db.Column(db.String())
    belonging = db.Column(db.String())
    user_id = db.Column(db.String())
    aim = db.Column(db.String())
    # 这是一个外键
    # user_id = db.Column(db.Integer, db.ForeignKey('stb_users.id'))
    # # relationship
    # reviews = db.relationship('Review', backref='chest')

    def __init__(self, form):
        print('chest init', form)
        self.name = form.get('name', '')
        self.content = form.get('content', '')
        self.status_list = form.get('status_list', json.dumps(dict()))
        self.paused = form.get('paused', '')
        self.belonging = form.get('belonging', '')
        self.status = form.get('status', 1)
        self.user_id = form.get("user_id", '')
        self.created_time = int(time.time())
        self.updated_time = int(time.time())
        self.user_id = form.get("user_id", '')
        self.aim = form.get("aim", 0)

    def _update(self, form):
        if form.get('status_list', ''):
            self.task = form.get('status_list', '')
        if form.get('aim', ''):
            self.aim = form.get('aim', '')

        self.save()
