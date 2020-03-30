from flasktodo import create_app

def test_config(monkeypatch):
    # Default config
    assert not create_app().testing

    # Test config
    assert create_app({'TESTING': True}).testing

    # Prod config
    monkeypatch.setenv('DATABASE_URL', "pretend this is on heroku...")
    assert "heroku" in create_app().config['DB_URL']
    assert "require" in create_app().config['DB_SSLMODE']

