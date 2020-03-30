# Flask To-Do

A simple to-do application written in Python using the [Flask web framework](https://flask.palletsprojects.com/en/1.1.x/) and [PostgreSQL](https://www.postgresql.org/).


## Installation

Fork this repo and use `git clone` to get a copy of your fork on your local machine, then create and activate a virtual environment to install the dependencies.

```sh
$ cd flask-todo
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Flask's environment variables can be set by running:

```sh
$ source bin/env.sh
```

Then you can run the shell script provided to create the database for the application:

```sh
$ sh bin/create-db.sh
```

To create the tables, you can run the following command. You'll need to run this again for any changes to `schema.sql`.

```sh
$ flask init-db
```

## Running the Application

```sh
$ flask run
```

You should be able to view the app at [http://localhost:5000]().

