from models.todo import Todo
from routes import *


main = Blueprint('todo', __name__)

Model = Todo


@main.route('/')
def index():
    ms = Model.query.all()
    return render_template('todo_index.html', todo_list=ms)



@main.route('/edit/<id>')
def edit(id):
    m = Model.query.get(id)
    return render_template('todo_edit.html', todo=m)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    Model.new(form)
    return redirect(url_for('.index'))


@main.route('/update/<id>', methods=['POST'])
def update(id):
    form = request.form
    Model.update(id, form)
    return redirect(url_for('.index'))


@main.route('/delete/<id>')
def delete(id):
    Model.delete(id)
    return redirect(url_for('.index'))
