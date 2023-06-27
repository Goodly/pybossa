docker-compose cp pybossa_db.sql pybossa-db:/pybossa_db.sql
docker-compose exec pybossa-db psql -U pybossa -d pybossa -f pybossa_db.sql
