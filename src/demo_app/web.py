"""Simple Flask web application exposing a landing page and health check."""
from __future__ import annotations

import os
from typing import Any, Dict

from flask import Flask, Response, jsonify, render_template_string, request, url_for

from . import __version__


LANDING_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Demo CI/CD App</title>
    <style>
      :root {
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }
      body {
        margin: 0;
        background: #0f172a;
        color: #e2e8f0;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
      }
      .card {
        background: rgba(15, 23, 42, 0.85);
        border-radius: 16px;
        padding: 2.5rem;
        max-width: 32rem;
        text-align: center;
        box-shadow: 0 20px 40px rgba(15, 23, 42, 0.4);
      }
      h1 {
        margin-bottom: 0.75rem;
        font-size: clamp(2rem, 5vw, 2.8rem);
      }
      p {
        margin-bottom: 1.5rem;
        line-height: 1.5;
      }
      .cta {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.75rem 1.75rem;
        background: #38bdf8;
        color: #0f172a;
        border-radius: 999px;
        text-decoration: none;
        font-weight: 600;
        transition: transform 120ms ease, box-shadow 120ms ease;
      }
      .cta:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 24px rgba(56, 189, 248, 0.35);
      }
      .meta {
        margin-top: 1.75rem;
        font-size: 0.85rem;
        color: rgba(226, 232, 240, 0.7);
      }
      code {
        font-size: 0.9rem;
        padding: 0.2rem 0.4rem;
        background: rgba(226, 232, 240, 0.08);
        border-radius: 6px;
      }
    </style>
  </head>
  <body>
    <main class="card">
      <h1>Ready for CI/CD</h1>
      <p>
        Deploy this demo service to a Kubernetes cluster and use it as a teaching aid for
        DevOps fundamentals. The app ships with automated tests, linting, and a GitHub
        Actions workflow.
      </p>
      <a class="cta" href="{{ docs_url }}">View Usage Notes</a>
      <div class="meta">
        <p>Version <code>{{ version }}</code></p>
        <p>Health endpoint: <code>{{ health_url }}</code></p>
        <p>Client IP: <code>{{ client_host }}</code></p>
      </div>
    </main>
  </body>
</html>
"""


DOCS_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Demo CI/CD App — Usage</title>
    <style>
      :root {
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }
      body {
        margin: 0 auto;
        padding: clamp(1.5rem, 4vw, 3rem);
        max-width: 60rem;
        line-height: 1.65;
        color: #0f172a;
        background: #f8fafc;
      }
      h1,
      h2 {
        color: #1e293b;
      }
      code {
        background: rgba(15, 23, 42, 0.08);
        padding: 0.2rem 0.4rem;
        border-radius: 4px;
      }
      pre {
        background: rgba(15, 23, 42, 0.08);
        padding: 1rem;
        border-radius: 8px;
        overflow: auto;
      }
      a {
        color: #2563eb;
      }
    </style>
  </head>
  <body>
    <h1>Usage notes</h1>
    <p>
      This lightweight Flask application is intentionally small so you can demo CI/CD and
      Kubernetes deployment workflows.
    </p>
    <h2>Endpoints</h2>
    <ul>
      <li><code>{{ landing_url }}</code> — landing page suitable for external exposure.</li>
      <li><code>{{ health_url }}</code> — JSON health check for readiness/liveness probes.</li>
      <li><code>{{ docs_url }}</code> — this page.</li>
    </ul>
    <h2>Running locally</h2>
    <pre><code>export FLASK_APP=demo_app.web:create_app
flask run --host=0.0.0.0 --port=8000
# or
python -m demo_app.web
</code></pre>
    <h2>Configuration</h2>
    <p>
      The server honours the <code>PORT</code> environment variable, defaulting to
      <code>8000</code>. For production, set this to the container port exposed by your
      platform (e.g. Kubernetes Service).
    </p>
    <p>Include the package path via <code>PYTHONPATH=src</code> when running from
      the repository root.</p>
    <h2>Version</h2>
    <p>Application version: <code>{{ version }}</code></p>
  </body>
</html>
"""


def create_app() -> Flask:
    """Create and configure the Flask app."""
    app = Flask(__name__)

    @app.get("/")
    def landing() -> Response:
        context: Dict[str, Any] = {
            "version": __version__,
            "docs_url": url_for("docs", _external=True),
            "health_url": url_for("health_check", _external=True),
            "client_host": request.remote_addr or "unknown",
        }
        return render_template_string(LANDING_TEMPLATE, **context)

    @app.get("/docs")
    def docs() -> Response:
        context: Dict[str, Any] = {
            "version": __version__,
            "landing_url": url_for("landing", _external=True),
            "health_url": url_for("health_check", _external=True),
            "docs_url": url_for("docs", _external=True),
        }
        return render_template_string(DOCS_TEMPLATE, **context)

    @app.get("/healthz")
    def health_check() -> Response:
        payload = {"status": "ok", "version": __version__}
        return jsonify(payload)

    return app


def main() -> None:
    app = create_app()
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":  # pragma: no cover - for `python -m demo_app.web`
    main()
