
# Instroduction

This project is a simple note web app, just a learning material using [FastAPI](https://fastapi.tiangolo.com/) and [Vue3](https://vuejs.org/). I get the inspiration from [testdrivenio / fastapi-vue](https://github.com/testdrivenio/fastapi-vue) but has something different with it.

# Frontend

I use **Vue3** in the composition API of `<script setup>`.  Subtitute [Pinia](https://pinia.vuejs.org/index.html) for Vuex and use the [Vue Router](https://router.vuejs.org/) of version 4.

## Setup

Install dependencies:

```bash
$ npm install
```

# Backend

The ORM tool is the [sqlalchemy](https://www.sqlalchemy.org/) and the migration tool the [alembic](https://alembic.sqlalchemy.org/en/latest/).

## Migrations

Modify the value of `sqlalchemy.url` in file `alembic.ini`:

```
sqlalchemy.url = mysql+pymysql://username:password@ip/database_name
```

Generate the migration script:

```bash
$ alembic revision -m --autogenerate "comment"
```

Run the migration:

```bash
$ alembic upgrade head
```

# Deployment with nginx

Run the FastAPI:

```bash
$ uvicorn app.main:app
```

Start the nginx

```bash
$ systemctl start nginx
```






