#!/bin/bash
cp settings_local.py.tmpl settings_local.py &&  cp alembic.ini.template alembic.ini
sed -i 's/pybossa:tester@localhost/pybossa:tester@pybossa-db/' settings_local.py && sed -i 's/pybossa:tester@localhost/pybossa:tester@pybossa-db/' alembic.ini && sed -i "s/REDIS_SENTINEL = \[('localhost', 26379)\]/REDIS_SENTINEL = \[('redis-sentinel', 26379)\]/" settings_local.py
