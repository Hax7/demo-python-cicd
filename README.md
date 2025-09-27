# Demo CI/CD Python Service

This repository contains a tiny Python web service and an accompanying GitHub Actions workflow that you can use to demonstrate the basics of continuous integration and deployment. It exposes a simple landing page so you can publish it to a Kubernetes cluster and view it from the internet.

## Project layout

- `src/demo_app/logic.py` – example business logic with unit tests.
- `src/demo_app/web.py` – Flask application providing a landing page, `/docs`, and `/healthz` endpoints.
- `tests/` – pytest suite covering the business logic and web routes.
- `.github/workflows/ci.yml` – GitHub Actions pipeline that installs dependencies, runs linting (flake8), and executes the pytest suite.
- `Dockerfile` – container image that serves the Flask app on port 8000.
- `k8s/` – starter Deployment and Service manifests you can tweak when deploying to Kubernetes.

## Quick start

1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the test suite locally:
   ```bash
   pytest
   ```
4. Start the web server:
   ```bash
   PYTHONPATH=src python -m demo_app.web
   # or using Flask's CLI
   FLASK_APP=demo_app.web:create_app PYTHONPATH=src flask run --host=0.0.0.0 --port=8000
   ```
   Visit http://127.0.0.1:8000/ to view the landing page.

## Container image

Build and run the Docker image locally:

```bash
docker build -t demo-app:local .
docker run --rm -p 8000:8000 demo-app:local
```

The container listens on `0.0.0.0:8000` and honours the `PORT` environment variable for platform overrides.

## Kubernetes starter manifests

The `k8s/` directory provides a minimal Deployment and LoadBalancer Service. Update the `image` reference to point at the container registry you push to (e.g., `ghcr.io/<org>/<repo>:<tag>`), then apply the manifests:

```bash
kubectl apply -f k8s/
```

These manifests configure readiness/liveness probes against `/healthz`, mirroring the automated health check.

## Teaching notes

- The `ci.yml` workflow is intentionally compact so students can understand each step quickly.
- The project ties together unit tests, linting, containerisation, and Kubernetes manifests—perfect ingredients for a small CI/CD lab.
- Extend the workflow with additional jobs (e.g., image build, deploy) as course exercises.

## Releasing updates

When you push changes to GitHub, the CI workflow runs automatically on the latest code. Pull requests will show the workflow status, reinforcing the DevOps practice of automated verification. You can later add jobs that build the Docker image and deploy the manifests for a full CD story.
# demo-python-cicd
