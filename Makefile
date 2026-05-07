mig:
	python manage.py makemigrations
	python manage.py migrate

# python manage.py dumpdata --indent 4 apps.Post > posts.json
# python manage.py loaddata posts