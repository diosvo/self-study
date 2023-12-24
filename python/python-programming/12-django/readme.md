# Django

Intro to Django Web Development

This mini-project will include:

- 94 - Intro to Django Web Development
- 95 - Creating a Django Hello World App
- 96 - Django Database Migrations
- 97 - Working with Django Database in Shell
- 98 - Displaying Database Data in HTML - Django
- 99 - Parameter URLs and Dynamic Links

# How to use

Download `get-pip.py`:

```bash
curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

Download the virtual environment package:

```bash
sudo pip install virtualenv
```

Create a virtual environment:

```bash
virtualenv env
```

Access the virtual environment:

```bash
source env/bin/activate
```

> Exit the virtual environment with `deactivate` command

Install `django` package in the virtual environment:

```bash
python3 -m pip install django
```

Start a new project:

```bash
django-admin startproject books
```

> Remember to direct to <project_name> before running the commands below.

| Description         | Command                                       |
| :------------------ | :-------------------------------------------- |
| Open the shell      | `python3 manage.py shell`                     |
| Start the server    | `python3 manage.py runserver`                 |
| Start specific app  | `python3 manage.py startapp <app_name>`       |
| Migrate application | `python3 manage.py migrate`                   |
| Apply the changes   | `python3 manage.py makemigrations <app_name>` |
