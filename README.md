# EmPath - Employment Pathway

Empath is a cross-platform desktop program for keeping track of a Software Engineer's job applications. We make no guarantees of job placement, simply to help you on yur Employment Pathway at a startup or maybe even Morgan Polysoft.

## Getting Started

Empath is written in [_Python_](https://www.python.org/downloads/), with [_Django_](https://www.djangoproject.com/) and [_FlaskWebGUI_](https://github.com/ClimenteA/flaskwebgui).

With [_uv_](https://docs.astral.sh/uv/getting-started/installation/) installed, simply run

```sh
uv sync
```

to install all required dependencies in a Python virtual environment.

Then run

```sh
uv run python3 manage.py migrate
```

to build the database, followed by

```sh
uv run python3 manage.py createsuperuser
```

to create your account.

The application uses _Django_'s built-in Admin Panel to perform some functions. The account created here can be accessed either directly from the _Admin Panel_ button on the left of the UI, or from various CRUD buttons displayed on various pages, usually labeled _Add_ or _Update_.

To run the application itself use

```sh
uv run python3 gui.py
```
