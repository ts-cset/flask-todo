from flask import Blueprint, render_template, request

from . import db
import psycopg2
import psycopg2.extras


bp = Blueprint("todos", __name__)


@bp.route("/", methods=('GET', 'POST'))
def index():
    """View for home page which shows list of to-do items."""

    if request.method == 'POST':
        # the variable addTask is equal to the form data on index.html
        addTask = request.form['addTask']
        # get the database connection
        with db.get_db() as con:
            # Begin the transaction
            with con.cursor() as cur:
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
