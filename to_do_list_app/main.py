from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_login import login_required, current_user
import unittest

from app import create_app
from app.forms import TodoForm
from app.firestore_service import get_users, get_todos, put_todo, delete_todo

app = create_app()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('hello'))
    session['user_ip'] = user_ip
    return response


@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()
    context = {
        'user_ip': user_ip,
        'todos': get_todos(username),
        'username': username,
        'todo_form': todo_form,
    }
    if todo_form.validate_on_submit():
        put_todo(username, todo_form.description.data)
        flash('Task created')
        return redirect(url_for('hello'))
    return render_template('hello.html', **context)


@app.route('/todos/delete/<todo_id>', methods=['GET', 'POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id, todo_id)
    flash('Task deleted')
    return redirect(url_for('hello'))
