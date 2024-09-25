# [django-base-template](https://github.com/ibraheem4/django-base-template) &middot; [![Continuous Integration](https://github.com/ibraheem4/django-base-template/actions/workflows/ci.yml/badge.svg)](https://github.com/ibraheem4/django-base-template/actions?query=workflow%3A%22Continuous+Integration%22)

_NOTE:_ This app runs on SSL, so the default commands (e.g. `pnpm start`) will serve via HTTPS on localhost.

## Prerequisites [](#prerequisites)

Before running this application, ensure that you have the following installed:

- [Git](https://git-scm.com/)
- [Node.js 22.9.0](https://nodejs.org/)
- [pnPM](https://pnpm.io)
- [Django](https://www.djangoproject.com/)
- [Python 3.12.6](https://www.python.org/downloads/)
- [Pipenv](https://pypi.org/project/pipenv/)
- [Google Chrome](https://google.com/chrome/)
- [Homebrew](https://brew.sh)

## Installation

1. Clone the repository or download the source code.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run `pnpm install` to install the project dependencies.

## Quickstart [](#quickstart)

### Update Environment Variables [](#update-environment-variables)

Include `.env` file to set environment variables. `.env.example` is included as an example.

### Update FIXME [](#update-fixme)

Find and replace any instances of `FIXME`.

### Run startup scripts [](#run-startup-scripts)

```
sh scripts/ssl-script.sh && \ # Only on initial setup
sh scripts/startup-script.sh
```

1. Generate SSL scripts
2. Install Python packages
3. Migrate databases
4. Collect static files
5. Load fixtures
6. Run the server

Verify project is serving on localhost.

- Visit your API at [https://localhost:8000/api](https://localhost:8000/api)
- Visit the Django admin at [https://localhost:8000/admin](https://localhost:8000/admin)

## Running / Development [](#running-developing)

### Setup Database [](#setup-database)

Generate a SQLite database (`django_base_template/django_base_template/db.sqlite3`) and load initial fixture data.

- `pnpm migrate:run-syncdb`
- `pnpm load-fixtures`

### Collect static files [](#collect-static-files)

Run the `collectstatic` management command.

- `pnpm collectstatic`

> Visit your API at [https://localhost:8000/api](https://localhost:8000/api)

### Testing [](#testing)

Run some tests.

- `pnpm test`
- `pnpm coverage:html`

> Open `htmlcov/index.html` in the web browser.

### Linting [](#linting)

Perform linting.

- `pnpm lint`

### Git commit template [](#git-commit-template)

    git config commit.template .gitmessage

## Further Reading / Useful Links [](#further-reading-useful-links)

- [Conventional Commits](https://www.conventionalcommits.org)
- [The Twelve-Factor App](https://12factor.net)
- [Daphne](https://github.com/django/daphne)
- [GitHub Actions](https://github.com/features/actions)
- [Husky](https://typicode.github.io/husky/)
- [Pipenv](https://pypi.org/project/pipenv/)
- [Pytest](https://docs.pytest.org/en/stable/)
