# django-base-template

*NOTE:* This app runs on SSL, so the default commands (e.g. `yarn start`) will serve via HTTPS on localhost.

## Prerequisites [](#prerequisites)

1. Buy an Apple computer.
2. Install the following on your computer.

- [Git](https://git-scm.com/)
- [Node.js](https://nodejs.org/)
- [Yarn](https://yarnpkg.com/)
- [Django](https://www.djangoproject.com/)
- [Python](https://www.python.org/)
- [Pipenv](https://pypi.org/project/pipenv/)
- [Google Chrome](https://google.com/chrome/)
- [Homebrew](https://brew.sh)
- [Perl](https://www.perl.org)
- [hub](https://github.com/github/hub)

## Spawning a new project [](#spawning-a-new-project)

**Spawn a new project from this template.**

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

## Quickstart [](#quickstart)

Generate SSL scripts, install Python packages, migrate databases, collect static files, run  the server.

```
yarn generate-ssl && \
yarn pipenv:install && \
yarn migrate:run-syncdb && \
yarn collectstatic && \
yarn start
```

Verify project is serving on localhost.

- Visit your API at [https://localhost:8000/api](https://localhost:8000/api)
- Visit the Django admin at [https://localhost:8000/admin](https://localhost:8000/admin)

## Running / Development [](#running-developing)

### Running the template itself [](#running-the-template-itself)

The template variables must first be replaced with a valid project name (e.g. `project_name`) to run the `django-base-template` project itself.

#### Update template variables [](#update-template-variables)

Run the `demo:update` command to update template variables in all files (excluding .git folder, README), then run the [quickstart](#quickstart) commands to start up the server.

- `yarn demo:update`
- Run [quickstart](#quickstart)

#### Restore template variables [](#restore-template-variables)

Run the `demo:restore` command to restore the template variables after running the `django-base-template` project.

**IMPORTANT:** do this before committing to version control to ensure template variables have not been changed.

- `yarn demo:restore`

### Include `.env` [](#include-dotenv)

Include `.env` file to set environment variables.  `.env.example` is included as an example.

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

> Open `htmlcov/index.html` in the web browser.

### Linting [](#linting)

Perform linting.

- `yarn lint`

### Git commit template [](#git-commit-template)

    git config commit.template .gitmessage