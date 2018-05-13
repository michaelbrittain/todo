# Todo List

A simple todo list app written in Python3/Django

### Prerequisites

virtualenv, python3

### Installing

From the project root folder:

virtualenv -p python3.6 venv

. venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

### Setup

Run fixtures to create initial data:

python manage.py loaddata users tasks

### Running

python manage.py runserver

Then [open in browser](http://localhost:8000)

The fixtures data includes 2 users - alice and bob, with password H8ppyD8ys

Click 'Login' at the top right to sign in.

Alternatively, clicking on any action will redirect you to login.

## Running the tests

coverage run ./manage.py test

coverage report

## To use Django admin

python manage.py createsuperuser

python manage.py runserver

Then [open in browser](http://localhost:8000/admin/)

## Author

* **Mike Brittain** - [GitHub](https://github.com/michaelbrittain)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
