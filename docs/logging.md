# Logging Strategy

- FastAPI application logs are available using:

```bash
docker compose logs fastapi
```

- NGINX logs:

```bash
docker compose logs nginx
```

- PostgreSQL logs:

```bash
docker compose logs postgres
```

- Redis logs:

```bash
docker compose logs redis
```

For production, centralized logging can be implemented using ELK Stack or Grafana Loki.