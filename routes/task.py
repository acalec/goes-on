from models.task import Task
from routes import *
from utils.utils import log
import json
import datetime
import calendar
from routes.user import current_user, login_check
from utils.for_task import sum_lists

main = Blueprint('task', __name__)

Model = Task


def cal_list():
    month = datetime.datetime.now().strftime('%m')
    year = datetime.datetime.now().strftime('%Y')
    rs = calendar.monthcalendar(int(year), int(month))
    r = []
    for sr in rs:
        r.extend(sr)

    return r, month, year


@main.route('/')
def index():
    # print("enter task index")
    u = current_user()
    ms = Model.query.filter_by(user_id=u.id).all()
    # print(u, ms)
    # ms = Model.query.all()
    weeks, m, y = cal_list()
    # format_weeks = list(map())

    format_weeks = []
    for w in weeks:
        if w != 0 and int(w) < 10:
            w = '{0}-{1}-0{2}'.format(y, m, str(w))
            format_weeks.append(w)
        elif w != 0:
            w = '{0}-{1}-{2}'.format(y, m, str(w))
            format_weeks.append(w)

    sl_dict = dict()
    sum_dict = dict()
    achieved_dict = dict()
    sum_values = []
    if ms:
        for m in ms:
            sl = json.loads(m.status_list)
            status_list_dict = dict()
            sld = status_list_dict
            sls = []
            for fw in format_weeks:
                if fw in sl.keys():
                    sld[fw] = sl[fw]
                    sls.append(sl[fw])
                else:
                    sld[fw] = 0
                    sls.append(0)
            sl_dict[m.id] = sls
            print("sls", sls)
            sum_dict[m.id] = sum(sls)
            achieved_dict[m.id] = int(int(m.aim) * len(weeks) * 4 / 7)
            print("in sys", sl_dict)
        print("out sys", sl_dict)

        ss = sl_dict
        sum_values = sum_lists(list(ss.values()))
        print("out sys", sl_dict)

    print("sl_dict", sl_dict)
    # sl_dict = json.dumps(sl_dict)
    # print(sl_dict)
    # fw = list(map(lambda x: x[5:], format_weeks))
    return render_template(
        'task/indexx.html',
        task_list=ms,
        sum_values=sum_values,
        user=u,
        weeks=format_weeks,
        status_lists=sl_dict,
        achieved_dict=achieved_dict,
        sum_dict=sum_dict)


@main.route('/profile')
def profile():
    # print("enter task index")
    u = current_user()
    ms = Model.query.filter_by(user_id=u.id).all()

    return render_template('task/profile.html', task_list=ms)


@main.route('/edit/<id>')
def edit(id):
    m = Model.query.get(id)
    return render_template('task/edit.html', task=m)


@main.route('/add', methods=['POST'])
def add():
    u = current_user()
    form = request.form
    m = Model.new(form)
    m.user_id = u.id
    m.save()
    return redirect(url_for('.index'))


@main.route('/update/<id>', methods=['POST'])
def update(id):
    form = request.form
    Model._update(id, form)
    return redirect(url_for('.index'))


@main.route('/update/target/<id>', methods=['POST'])
def update_target(id):
    form = request.form
    Model.update(id, form)
    return redirect(url_for('.index'))


@main.route('/delete/<id>')
def delete(id):
    Model.delete(id)
    return redirect(url_for('.index'))


@main.route('/init/1')
def init():
    id = 1
    Model = Task
    t = Model.query.get(id)
    c = t.status_list
    log("C", c, type(c), json.loads(c), type(json.loads(c)))
    d = {
        '2018-07-01': '2',
        '2018-07-02': '4',
        '2018-07-04': '1',
        '2018-07-03': '2',
    }
    d = json.dumps(d)
    t.status_list = str(d)
    t.save()


@main.route('/go/<id>', methods=['GET'])
def go(id):
    w = Task.query.get(id)
    print("w", w)
    # u = current_user()
    # print('w', w)
    temp = json.loads(w.status_list)
    date_now = datetime.datetime.now().strftime('%Y-%m-%d')
    date_now = str(date_now)
    if date_now in temp.keys():
        temp[date_now] = int(temp[date_now]) + 1

    else:
        temp[date_now] = 1
    w.status_list = json.dumps(temp)
    w.save()
    return redirect(url_for('.index'))
    # return api_response(True, data=w)
