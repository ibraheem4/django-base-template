# django-base-template

*NOTE:* This app is designed to run on SSL, so the default commands (e.g. `yarn start`) will serve via HTTPS on localhost.

# Generate new project [](#generate-new-project)

**Generate a new project from this template.**

For example, for a project named `django_template_demo` in a directory called `django-template-demo`, run these commands:

```
mygitg && \
mkdir django-template-demo && \
cd django-template-demo && \
django-admin startproject --template=https://github.com/ibraheem4/django-base-template/archive/master.zip django_template_demo . && \
find . -not -iwholename '*.git*' -type f -print0 | xargs -0 perl -pi -w -e 's/\{\{ project_name \}\}/django_template_demo/g;' \ && \
git init && \
hub create -p && \
git add --all && \
git commit -m "Initial commit" && \
git push origin master && \
hub browse
```

# Run this project [](#run-this-project)

**Update template variables in all files, then run [quickstart](#quickstart)**

```
find . -not -iwholename '*.git*' -type f -print0 | xargs -0 perl -pi -w -e 's/\{\{ project_name \}\}/project_name/g;' \
```

**Undo updating of template variables**

```
find . -not -iwholename '*.git*' -type f -print0 | xargs -0 perl -pi -w -e 's/project_name/\{\{ project_name \}\}/g;' \
```

# Quickstart [](#quickstart)

`yarn generate-ssl && yarn pipenv:install && yarn migrate:run-syncdb && yarn collectstatic && yarn start`

- user: `test@test.com`, pass: `TestPassword`
- Visit your API at [https://localhost:8000/api](https://localhost:8000/api)
- Visit the Django admin at [https://localhost:8000/admin](https://localhost:8000/admin)


## Prerequisites [](#prerequisites)

You will need the following things installed on your computer.

- [Git](https://git-scm.com/)
- [Node.js](https://nodejs.org/)
- [Yarn](https://yarnpkg.com/)
- [Django](https://www.djangoproject.com/)
- [Python](https://www.python.org/)
- [Pipenv](https://pypi.org/project/pipenv/)
- [Google Chrome](https://google.com/chrome/)
- [Homebrew](https://brew.sh)

## Installation [](#installation)

After cloning the repository, install Python packages using `pipenv`.

- `git clone <repository-url>`
- `cd {{ project_name }}`
- `yarn generate-ssl` (installs `mkcert` via `homebrew` then generates a public/private key pair at `ssl/`)
- `yarn pipenv:install` (installs Python virtual environment at `{{ project_name }}/.venv`)

## Running / Development [](#running-developing)

### Setup Database [](#setup-database)

Generate a SQLite database (`django_base_template/django_base_template/db.sqlite3`) and load initial fixture data.

- `yarn migrate:run-syncdb`
- `yarn load-initial-data`

### Collect static files [](#collect-static-files)

Run the `collectstatic` management command.

- `yarn collectstatic`

> Visit your API at [https://localhost:8000/api](https://localhost:8000/api)

### Testing [](#testing)

Run some tests.

- `yarn test`
- `yarn coverage:html`

> Open `htmlcov/index.html` in web browser.

### Linting [](#linting)

Perform linting.

- `yarn lint`

### Include `.env` [](#include-dotenv)

Include `.env` file to set environment variables.  `.env.example` is included as an example.

### Using the Git commit template

    git config commit.template .gitmessage