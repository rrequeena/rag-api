#!/bin/bash
set -e

# Wait for PostgreSQL to start
until psql -h "$POSTGRES_HOST" -U "$POSTGRES_USERNAME" -d "$DATABASE_NAME" -c '\q'; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

# Create the vector extension
psql -h "$POSTGRES_HOST" -U "$POSTGRES_USERNAME" -d "$DATABASE_NAME" -c "CREATE EXTENSION IF NOT EXISTS vector;"
