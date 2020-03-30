import pytest

from flasktodo import create_app
from flasktodo import db


@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'DB_URL': "postgresql://flasktodo_user@localhost/flasktodo_test"
    })

    with app.app_context():
        db.init_db()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

