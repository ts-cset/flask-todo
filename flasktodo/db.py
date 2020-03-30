import os
import psycopg2

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """Get a PostgreSQL database connection object."""

    # This function returns a connection, but you will also need to open a
    # cursor for the given transaction. For SELECT queries, it would look like:
    #
    # with get_db().cursor() as cur:
    #     cur.execute("SELECT ...")

    if 'db' not in g:
        # if there is not already a connection, open one using app
        # configuration and save it to global `g` object
        g.db = psycopg2.connect(
            current_app.config['DB_URL'],
            sslmode=current_app.config['DB_SSLMODE'],
        )

    return g.db


def close_db(e=None):
    """Close the current PostgreSQL connection"""

    # remove connection object from global `g` object, if it exists
    db = g.pop('db', None)

    if db is not None:
        # close the connection
        db.close()


def init_db():
    """Create initial database schema."""

    # open the schema file and close it when done
    with current_app.open_resource('schema.sql') as f:
        # get the database connection, save and close when done
        with get_db() as con:
            # begin a transaction
            with con.cursor() as cur:
                # use the file's text to execute the SQL queries within
                cur.execute(f.read())
        

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear any existing data and create all tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    """Register database functions with app."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

