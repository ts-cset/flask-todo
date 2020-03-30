import psycopg2
import pytest

from flasktodo.db import get_db


def test_get_db_then_close(app):
    with app.app_context():
        db = get_db()
        assert db is get_db(), 'get_db should always return the same connection'

    with pytest.raises(psycopg2.InterfaceError) as error:
        cur = db.cursor()
        cur.execute('SELECT 1')

    assert 'closed' in str(error), 'connection should be closed after app context'


def test_init_db_cli_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('flasktodo.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called

