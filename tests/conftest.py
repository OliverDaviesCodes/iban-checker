from flask import Flask
from api import app
import pytest

@pytest.fixture()
def app():
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


