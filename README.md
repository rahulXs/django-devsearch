## django-devsearch

A platform for developers to create profile, list out projects, search other developers and their projects. Kind of a social media application for developer community.

#### Features

- Create profiles
- Search for other developers by name, technology etc
- Search for projects by name, technology etc
- Vote and review a project
- Send and receive messages (Inbox feature)

## Installation

Create and activate virtualenv `devsearch`:

```bash
virtualenv ~/virtualenvs/devsearch
. ~/virtualenvs/devsearch/bin/activate
```

Install required packages in virtualenv:

```bash
pip install -r requirements.txt
```

## Schema Design

Refer to [drawsql.app django-devsearch-schema](https://drawsql.app/self-122/diagrams/django-devsearch-schema)

![Schema design](https://github.com/rahulXs/django-devsearch/blob/main/drawSQL-export.png?raw=true)

## Usage

```bash
# Start django server 
python manage.py runserver
```

## Reference
Django Devsearch tool by Dennis Ivy.
