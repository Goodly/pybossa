FROM python:3.8
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get upgrade -y && apt-get install -y git libpq-dev python3-psycopg2 libsasl2-dev libldap2-dev libssl-dev python3-dev python-dev-is-python3 build-essential libjpeg-dev libssl-dev libffi-dev
RUN pip install -r requirements.txt && pip install SQLAlchemy==1.3.0
