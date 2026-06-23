# Deployment Guide

## Prerequisites

- Docker
- Docker Compose

## Build

```bash
docker compose up --build -d
```

## Verify

```
http://localhost:8080
```

```
http://localhost:8080/health
```

```
http://localhost:8080/docs
```

## Production Steps

- Install Docker
- Clone Repository
- Configure .env
- Run docker compose up -d --build

## SSL

Configure NGINX with Let's Encrypt certificates.

## Security

- Firewall (UFW)
- Fail2Ban
- SSH Key Authentication

## Restart Strategy

Containers use Docker restart policy.

## Backup

Database uses Docker Volume.