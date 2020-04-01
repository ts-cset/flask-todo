from flask import Blueprint, render_template, request

from . import db
import psycopg2
import psycopg2.extras


bp = Blueprint("todos", __name__)


@bp.route("/", methods=('GET', 'POST'))
def index():
    """View for home page which shows list of to-do items."""

    if request.method == 'POST':
        # the variable filterFeature is equeal to the from data on filterForm
        # get the database connection
        with db.get_db() as con:
            # Begin the transaction
            with con.cursor() as cur:
                # the variable filter feature is equal to the form dropDown
                filterFeature = request.form['dropDown']
                # code only runs if the request is toDo
                if filterFeature == 'toDo':
                    # only displays todos with a completed field of false
                    cur.execute(
                        'SELECT * FROM todos WHERE completed = False')
                    todos = cur.fetchall()
                    cur.close()
                # code only runs if the request is finished
                if filterFeature == 'finished':
                    # only displays todos with a completed field of true
                    cur.execute(
                        'SELECT * FROM todos WHERE completed = True ')
                    todos = cur.fetchall()
                    cur.close()
                # code only runs if the request is addTasks
                if filterFeature == 'allTasks':
                    # Displays all the to-dos on the index.html
                    cur.execute('SELECT * FROM todos')
                    todos = cur.fetchall()
                    cur.close()

                return render_template("index.html", todos=todos)

    cur = db.get_db().cursor()
    cur.execute('SELECT * FROM todos')
    todos = cur.fetchall()
    cur.close()
    return render_template("index.html", todos=todos)


@bp.route('/addATask', methods=('GET', 'POST'))
def adding_A_Task():
    """Adding a task function so the user can update their to-dos"""
    if request.method == 'POST':
        # get the database connection
        with db.get_db() as con:
            # Begin the transaction
            with con.cursor() as cur:
                # the variable addTask is equal to the form data on addTask
                addTask = request.form['addTask']
                # Inserts the description the user filled into the form using SQL
                cur.execute("""INSERT INTO todos (description, completed, created_at)
                VALUES (%s, %s, NOW())
                """,
                            (addTask, False)
                            )

    # Displays all the to-dos on the index.html
    cur = db.get_db().cursor()
    cur.execute('SELECT * FROM todos')
    todos = cur.fetchall()
    cur.close()

    return render_template("index.html", todos=todos)


@bp.route('/Edit', methods=('GET', 'POST'))
def Editing_feature():
    """So the user can change the description of a To Do item"""
    if request.method == 'POST':
        # get the database connection
        with db.get_db() as con:
            # Begin the transaction
            with con.cursor() as cur:
                # the variable EditDesc is equal to the form data of EditForm
                EditDesc = request.form['EditDesc']
                EditId = request.form['EditButton']

                # Changes the description the user filled into the form using SQL
                cur.execute(""" UPDATE todos
                            SET description = %s
                            WHERE id = %s
                            """,
                            (EditDesc, EditId,))
                con.commit()

    # Displays all the to-dos on the index.html
    cur = db.get_db().cursor()
    cur.execute('SELECT * FROM todos')
    todos = cur.fetchall()
    cur.close()

    return render_template("index.html", todos=todos)
