FROM python:3.9

COPY ./requirements.txt /requirements.txt


RUN pip install --upgrade pip \
    && pip install -r /requirements.txt \
    && mkdir /ecommerce

COPY . /ecommerce
WORKDIR /ecommerce

EXPOSE 8000

CMD ["gunicorn" , "--bind", "0.0.0.0:8000", "ecommerce.wsgi:application"]
