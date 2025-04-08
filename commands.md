docker compose up
celery -A cfehome worker --beat -l info
python manage.py shell
python manage.py runserver
jupyter notebook

for windows

docker compose up
celery -A pialhome worker -l info

celery -A pialhome beat -l info  
celery -A pialhome worker --pool=solo -l info
