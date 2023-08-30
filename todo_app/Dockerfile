FROM python:3.10-slim

ARG USER=django
ARG GROUP=django
ARG UID=1000
ARG GID=1000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev musl-dev libpq-dev gcc
RUN apt-get install gettext -y
RUN groupadd -g $GID -o $USER && useradd -m -u $UID -g $GID -o -s /bin/bash $GROUP

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /code/
WORKDIR /code/
ADD . /code/

ENV DJANGO_SETTINGS_MODULE=todo_app.settings

USER ${USER}:${GROUP}

ENTRYPOINT ["./entrypoint.sh"]
