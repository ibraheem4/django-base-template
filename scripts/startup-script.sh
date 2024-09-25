#!/bin/bash

# Check if PostgreSQL is being used
if [ "$DB_ENGINE" = "django.db.backends.postgresql" ]; then
    echo "Using PostgreSQL. PostgreSQL dependencies are installed in Pipfile."
else
    echo "Using SQLite. PostgreSQL dependencies are available if needed."
fi

pnpm pipenv:install && \
pnpm migrate:run-syncdb && \
pnpm collectstatic && \
pnpm load-fixtures && \
pnpm start