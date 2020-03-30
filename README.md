# Flask To-Do

A simple to-do application written in Python using the [Flask web framework](https://flask.palletsprojects.com/en/1.1.x/) and [PostgreSQL](https://www.postgresql.org/).


## Instructions

You and a partner will work together to complete the [user stories in the documentation folder](docs/user-stories.md). Here are some helpful pieces of documentation:

- [GitHub: Syncing a fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork) - so you can keep your repo up to date with this one and your partner's
- [Psycopg: Basic Module Usage](https://www.psycopg.org/docs/usage.html) - to learn how to use the database functions


## Installation

Fork this repo and use `git clone` to get a copy of your fork on your local machine, then create and activate a virtual environment to install the dependencies.

```sh
$ cd flask-todo
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Then you can run the shell script provided to create the database for the application:

```sh
$ sh bin/create-db.sh
```

You need to set environment variables in your terminal session to use any of the following `flask` commands:

```sh
$ export FLASK_APP=flasktodo
$ export FLASK_ENV=development
```

To create the tables, you can run the following command. You'll need to run this again for any changes to `schema.sql`.

```sh
$ flask init-db
```

Mock data is stored in `tests/data.sql` and will be inserted into the test database for every test. If you would like to use the same data when developing, you can run this command to insert it into the development database.

```sh
$ flask mock-db
```


## Running the Application Locally

```sh
$ flask run
```

You should be able to view the app at [http://localhost:5000]().


## Run the Tests

```sh
$ coverage run -m pytest
$ coverage report
```

The first command runs your tests, while the second will show you a report of your total test coverage across all your modules. To generate a more detailed interactive report, run this command and view the result in your browser, which allows you to click on each module and see which lines need to be tested.

```sh
$ coverage html
$ open htmlcov/index.html
```


## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

If you've forked this repo, you can deploy your code by clicking the button above.

