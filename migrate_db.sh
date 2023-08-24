#!/bin/bash
sed -i "10s|.*|sqlalchemy.url = $DATABASE_URL|" alembic.ini
alembic upgrade head
