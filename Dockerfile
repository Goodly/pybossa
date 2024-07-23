FROM python:3.8-bullseye
WORKDIR /app
RUN apt-get update && apt-get upgrade -y && apt-get install -y git libpq-dev python3-psycopg2 libsasl2-dev libldap2-dev libssl-dev python3-dev python-dev-is-python3 build-essential libjpeg-dev libffi-dev
COPY ./requirements.txt /app/requirements.txt
COPY ./setup.py /app/setup.py
COPY ./setup.cfg /app/setup.cfg
COPY ./pybossa/version.txt /app/pybossa/version.txt
RUN pip install -r requirements.txt && pip install SQLAlchemy==1.3.0
COPY . /app
