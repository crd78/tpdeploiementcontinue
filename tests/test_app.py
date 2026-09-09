from app import app


class FakeCursor:
    def __init__(self, rows=None):
        self.rows = rows or []

    def execute(self, query):
        self.query = query

    def fetchone(self):
        return (1,)

    def fetchall(self):
        return self.rows


class FakeConnection:
    def __init__(self, rows=None):
        self.rows = rows

    def cursor(self, dictionary=False):
        return FakeCursor(self.rows)

    def close(self):
        pass


def test_health_returns_ok_when_database_is_available(monkeypatch):
    monkeypatch.setattr("app.database_status", lambda: 1)
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_clients_returns_database_rows(monkeypatch):
    rows = [{"id": 1, "name": "Alice Martin"}]
    monkeypatch.setattr("app.get_connection", lambda: FakeConnection(rows))
    response = app.test_client().get("/clients")
    assert response.status_code == 200
    assert response.get_json() == rows
