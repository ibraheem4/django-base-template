#/bin/bash

yarn generate-ssl && \
yarn pipenv:install && \
yarn migrate:run-syncdb && \
yarn collectstatic && \
yarn load-fixtures && \
yarn start
