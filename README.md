# DevOps FastAPI Assignment

## Project Overview

This project demonstrates a production-ready FastAPI deployment using Docker and Docker Compose.

## Tech Stack

- FastAPI
- Docker
- Docker Compose
- PostgreSQL
- Redis
- NGINX
- GitHub Actions

## Project Structure

```
devops-fastapi-assignment
│
├── .github
│   └── workflows
│       └── deploy.yml
├── app
├── docs
├── nginx
├── docker-compose.yml
├── .env
└── README.md
```

## Run Project

```bash
docker compose up --build -d
```

## API

Home

```
GET /
```

Health

```
GET /health
```

Swagger

```
/docs
```

## Containers

- FastAPI
- PostgreSQL
- Redis
- NGINX

## CI/CD

GitHub Actions automatically builds the Docker image whenever code is pushed to the main branch.

## Security

- Environment variables stored in .env
- Reverse proxy using NGINX
- Container restart policy enabled

## Backup Strategy

PostgreSQL data is stored using Docker Volumes.

## SSL

In production, SSL can be configured using Let's Encrypt with NGINX.

## Future Improvements

- Cloudflare
- Monitoring with Prometheus
- Grafana
- Zero Downtime Deployment