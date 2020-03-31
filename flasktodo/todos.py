from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from . import db

bp = Blueprint("todos", __name__)

@bp.route("/", methods=('GET', 'POST'))
def index():
    """View for home page which shows list of to-do items."""

    cur = db.get_db().cursor()
    cur.execute('SELECT * FROM todos')
    todos = cur.fetchall()
    cur.close()

    return render_template("index.html", todos=todos)

@bp.route("/completed", methods=['GET', 'POST'])
def completed():


    cur = db.get_db().cursor()

    cur.execute('SELECT * FROM todos WHERE completed = True')
    todos = cur.fetchall()
    cur.close()

    return render_template("index.html", todos=todos)


@bp.route("/uncompleted", methods=['GET'])
def uncompleted():


    cur = db.get_db().cursor()

    cur.execute('SELECT * FROM todos WHERE completed = FALSE')
    todos = cur.fetchall()
    cur.close()

    return render_template("index.html", todos=todos)
