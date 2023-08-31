# todo-app

## Description

Simple Todo App, which allow authenticated users to create cases, assign tasks to the created cases.

## Prerequisites

* Docker

* Docker compose

## Prepare environment

Make a copy of environment files from env files with .dist extension inside envs/ directory (django.env, postgres.env) and fill them with correct values

## Run project

After setting environmental variables, run command `docker-compose up -d`.

First run requires also create superuser which can be done using command `docker-compose exec api python3 manage.py createsuperuser` and following instruction.

Api is available on `localhost:8200`, admin panel `localhost:8200/admin`.
