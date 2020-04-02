from flask import Blueprint, render_template, request

from . import db
import psycopg2
import psycopg2.extras


bp = Blueprint("auth", __name__)


@bp.route("/login", methods=('GET', 'POST'))
def login_feature():
    """So a user can save data and come back too it"""
    if request.method == 'POST':
        # get the database connection
        with db.get_db() as con:
            # Begin the transaction
            with con.cursor() as cur:
                # the variable passIn is equal to form passInput
                passIn = request.form['passInput']
                # the variable emailIn is equal to form emailInput
                emailIn = request.form['emailInput']

                if passIn and emailIn:  # some how tell if they exist in database
                    print('hello')
                    # redirect to the users /
    return render_template("login.html")


@bp.route("/", methods=('GET', 'POST'))
def register_feature():
    """So an anonymous user can become a know user
    and save their data to the application"""
    if request.method == 'POST':
        # get the database connection
        with db.get_db() as con:
            # begin the transaction
            with con.cursor() as cur:
                # the variable passReg is equal to the form of passRegInput
                passReg = request.form['passRegInput']
                # the variable emailReg is equal to the form of emailRegInput
                emailReg = request.form['emailRegInput']

                if passIn and emailIn:

                    cur.execute("""INSERT INTO users (email, password)
                            VALUES (%s, %s)""",
                                (emailReg, passReg, )
                                )
                    con.commit()

    return render_template("register.html")
