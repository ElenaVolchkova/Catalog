FROM python:3
ENV env
WORKDIR /Catalog
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/