# Vivpro-Assignment

#### Requirements -
- Python 3.12
- Mysql 8.2.0
- React 18.2

#### Installation Guide -
- Install poetry. Read more at [https://python-poetry.org/docs/]
- After installing poetry, Go to VendorManagement directory and create a type `poetry shell`. This will create a new virtual environment.
- After this, make sure that you are in the directory where `pyproject.toml` is present and type `poetry install`. This will install all dependencies that are needed for running this application.
- Once everything is installed, type `python manage.py check` to ensure that this is working properly.
- Type `python manage.py migrate` to run all migrations
- Once migrations are completed successfully, type `python manage.py runserver` to start the django server
- I have added postman collection json in the repository. You can check that and use APIs accordingly.
- I have commited `settings.py` just for your convenience. On production project, we must not expose the `settings.py` file directly.
- Go to postman and use `{{base_url}}/core/normalize_json` API to dump the data in the database. For simplicity sake, we will be using sqlite

- Install React 18.2
- Go to <project-dir>/vivpro/static/frontend
- Install necesary pacakges using `yarn install`
- Run command `yarn start`. Doing so will run frontend server on http://localhost:3000
