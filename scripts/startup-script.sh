#!/bin/bash

# Check if PostgreSQL is being used
if [ "$DB_ENGINE" = "django.db.backends.postgresql" ]; then
    echo "Using PostgreSQL. PostgreSQL dependencies are installed in Pipfile."
else
    echo "Using SQLite. PostgreSQL dependencies are available if needed."
fi

yarn pipenv:install && \
yarn migrate:run-syncdb && \
yarn collectstatic && \
yarn load-fixtures && \
yarn start