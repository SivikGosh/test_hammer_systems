FROM python:3.13-alpine

WORKDIR /project

COPY ./project/ ./
COPY ./pyproject.toml .

RUN pip install .

RUN python manage.py collectstatic --noinput

CMD [ "gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000" ]
