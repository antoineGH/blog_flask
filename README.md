## Blog Flask

## Table of contents

-   [General info](#general-info)
-   [Technologies](#technologies)
-   [Setup](#setup)
-   [Screenshots](#screenshots)

## General info

Blog Flask is a Tech Blog with :

-   Authentication
-   Post Management
-   Password Reset
-   User Customisation

Blog Flask is using Python Flask with Jinja2 templates and Werkzeug. SQLalchemy interacts as an object-relational mapper with the database.

## Technologies

Project is created with:

-   Python v3.9.0
-   astroid v2.4.1
-   bcrypt v3.1.7
-   blinker v1.4
-   cffi v1.14.0
-   click v7.1.1
-   colorama v0.4.3
-   Flask v1.1.2
-   Flask-Bcrypt v0.7.1
-   Flask-Login v0.5.0
-   Flask-Mail v0.9.1
-   Flask-SQLAlchemy v2.4.1
-   Flask-WTF v0.14.3
-   isort v4.3.21
-   itsdangerous v1.1.0
-   Jinja2 v2.11.2
-   lazy-object-proxy v1.4.3
-   MarkupSafe v1.1.1
-   mccabe v0.6.1
-   Pillow v7.1.2
-   pycountry v19.8.18
-   pycparser v2.20
-   pylint v2.5.2
-   six v1.14.0
-   SQLAlchemy v1.3.16
-   toml v0.10.1
-   Werkzeug v1.0.1
-   wrapt v1.12.1
-   WTForms v2.2.1

## Setup

### On Windows:

Create Environnement Variable :

```
$ SECRET_KEY = '12345678912345678912345678912312' // input your own 32 digits secret key
$ MAIL_USERNAME = 'address@mail.com'
$ MAIL_PASSWORD = 'mailpassword'
```

In [config.py](./flask_blog/config.py) edit with your mail information

```
$ MAIL_SERVER = 'smtp.mail.com' // replace with your mail server
$ MAIL_PORT = 587 // replace with port
$ MAIL_USE_TLS = True // use TLS Boolean
```

### Import project

```
$ git clone https://github.com/antoineratat/blog_flask.git
$ py -3 -m venv venv
$ venv\Script\Activate
$ pip install -r requirements.txt
$ cd flask_blog
$ python .\run.py
```

### Initialize Database

```
$ venv\Script\Activate
$ python
$ python
$ from run import db
$ db.create_all()
$ exit()
```

## Screenshots

### Main Page

![Login Screenshot](https://github.com/antoineratat/blog_flask/blob/master/screenshots/1.PNG?raw=true)

### New Post

![Login Screenshot](https://github.com/antoineratat/blog_flask/blob/master/screenshots/2.PNG?raw=true)

### Post Content Preview

![Login Screenshot](https://github.com/antoineratat/blog_flask/blob/master/screenshots/3.PNG?raw=true)
