import os
from models.task import Task
from models.user import User
from routes import *
from routes.user import current_user

main = Blueprint('index', __name__)


@main.route('/')
def index():
    # cs = Comment.query.all()
    # us = User.query.all()
    u = current_user()
    if u is not None:
        return redirect(url_for('task.index'))
    else:
        return redirect(url_for('user.index'))
