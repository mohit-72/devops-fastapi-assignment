# Backup Strategy

## Database

PostgreSQL data is stored using Docker Volumes.

Backup command:

```bash
docker exec postgres_db pg_dump -U postgres devopsdb > backup.sql
```

Restore:

```bash
psql -U postgres devopsdb < backup.sql
```

## Containers

Containers automatically restart using:

```yaml
restart: always
```