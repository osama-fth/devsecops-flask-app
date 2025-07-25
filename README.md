# DevSecOps Flask App

A minimal Flask web app containerized with Docker and tested via GitHub Actions CI.

## Features
- 🐍 Flask backend
- 🐳 Dockerized
- ⚙️ GitHub Actions CI pipeline

## Run locally

```bash
docker build -t flask-app .
docker run -p 8080:8080 flask-app
```
Go to: http://localhost:8080
