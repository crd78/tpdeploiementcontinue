import pytest

from app import app

pytestmark = pytest.mark.e2e


class FakeCursor:
    def execute(self, query):
        self.query = query

    def fetchone(self):
        return (1,)

    def fetchall(self):
        return [{"id": 1, "name": "Alice Martin"}, {"id": 2, "name": "Bruno Durand"}]


class FakeConnection:
    def cursor(self, dictionary=False):
        return FakeCursor()

    def close(self):
        pass


def test_real_http_journey(monkeypatch):
    monkeypatch.setattr("app.database_status", lambda: 1)
    monkeypatch.setattr("app.get_connection", lambda: FakeConnection())
    client = app.test_client()

    health = client.get("/health")
    clients = client.get("/clients")

    assert health.status_code == 200
    assert health.get_json()["status"] == "ok"
    assert clients.status_code == 200
    assert len(clients.get_json()) >= 1
