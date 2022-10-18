docker-compose up -d
docker exec -it gpx-formatter_web_1 bash
python manage.py runserver