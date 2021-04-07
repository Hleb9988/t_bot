import os
from src.asgi import app
from starlette.testclient import TestClient

import pytest

data = {"bot_token": os.getenv('BOT_TOKEN'), "pythonpath": os.getenv('PYTHONPATH')}


@pytest.mark.functional
def test_app_local():
    client = TestClient(app)
    response = client.get('http://localhost:8000/config/')
    assert response.status_code == 200
    assert response.json() == data


def test_app_global():
    client = TestClient(app)
    response = client.get('https://botbot43.herokuapp.com/config/')
    assert response.status_code == 200
    assert response.json() == data
