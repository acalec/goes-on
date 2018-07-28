import os

from models.user import User
from routes import *
from utils.utils import log

main = Blueprint('user', __name__)

Model = User

uploads_dir = 'static/img/uploads/'

xfrs_dict = {
    'd40a58205d884331aa7f2a7304ad6345': 0,
}


def current_user():
    uid = session.get('user_id')
    # print('chest init', uid)
    if uid is not None:
        u = User.query.get(uid)
        return u
    else:
        return None


def random_string():
    import uuid
    return str(uuid.uuid4())


@main.route('/')
def index():
    u = current_user()
    if u is not None:
        return redirect(url_for('task.index'))
    ms = Model.query.all()
    xfrs = random_string()
    xfrs_dict[xfrs] = 0
    return render_template('user/index.html', xfrs=xfrs, user_list=ms)


def login_check(func):
    def wrapper(*arg):
        u = current_user()
        if u is None:
            return redirect(url_for('user.index'))
        else:
            print("username", u.username, u.id)
            func(*arg)
            # return func

    return wrapper


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    u = Model(form)
    user = User.query.filter_by(username=u.username).first()
    if user is not None and user.password == u.password:
        session['user_id'] = user.id
        u = current_user()
        u.status = 1
        u.save()
        # print('login successful')
        return redirect(url_for('task.index'))
    else:
        print('login unsuccessful')
        return redirect(url_for('.index'))


@main.route('/edit/<id>')
@login_check
def edit(id):
    m = Model.query.get(id)
    return render_template('user/edit.html', user=m)


@main.route('/quit')
def quit():
    u = current_user()
    u.status = 0
    u.save()
    session.pop('user_id')
    return redirect(url_for('.index'))


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    xfrs = form.get('xfrs')
    print("xfrs", xfrs)
    if xfrs in xfrs_dict:
        xfrs_dict.pop(xfrs)
        u = Model(form)
        status, msgs = u.valid()
        # if (status):
        if status:
            # log("valid", u.valid())
            Model.new(form)
            return redirect(url_for('.index'))
        else:
            return render_template('user/sign_up_again.html', msg=msgs)

    else:
        return 'ERROR LINK'


@main.route('/update/<id>', methods=['POST'])
def update(id):
    form = request.form
    Model.update(id, form)
    return redirect(url_for('.index'))


@main.route('/delete/<int:id>')
def delete(id):
    Model.delete(id)
    return redirect(url_for('.index'))


@main.route('/profile/<int:id>')
def profile(id):
    u = current_user()
    return render_template('user/profile.html', user_single=u)


@main.route('/upload/<int:id>', methods=['POST'])
def upload(id):
    print('upload')
    f = request.files.get('uploaded')

    # if f:
    if f:
        filename = f.filename
        print('filename, ', filename)
        import uuid
        filename = str(uuid.uuid4()) + '.' + filename.split('.')[-1]
        temp_dir = uploads_dir + str(id) + '/'
        if not os.path.exists(temp_dir):
            os.mkdir(temp_dir)
        path = temp_dir + filename
        f.save(path)

        u = current_user()
        u.avatar = filename
        u.save()
        return redirect(url_for('.profile', id=id))
    else:
        return redirect(url_for('.profile', id=id))


@main.route('/admin')
def admin():
    u = current_user()
    print("role", u.role)
    if int(u.role) == 1:
        ms = Model.query.all()
        return render_template('user/admin.html', user_list=ms)
    else:
        return '''NO PERMISSION'''
