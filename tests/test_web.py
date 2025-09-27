from __future__ import annotations

from flask.testing import FlaskClient

from demo_app.web import create_app


def test_landing_page_renders_and_mentions_version() -> None:
    app = create_app()
    client: FlaskClient = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Ready for CI/CD" in response.data
    assert b"Version" in response.data


def test_docs_page_lists_endpoints() -> None:
    app = create_app()
    client: FlaskClient = app.test_client()

    response = client.get("/docs")
    body = response.data.decode("utf-8")

    assert response.status_code == 200
    assert "/healthz" in body
    assert "Application version" in body


def test_health_check_returns_json() -> None:
    app = create_app()
    client: FlaskClient = app.test_client()

    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "version": "0.1.0"}
