FROM python:3.11

RUN mkdir /app
WORKDIR $/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip  install --upgrade pip

COPY ./backend/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./backend /app

COPY ./docker/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start


COPY ./docker/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

EXPOSE 8000

ENTRYPOINT [ "/entrypoint"]