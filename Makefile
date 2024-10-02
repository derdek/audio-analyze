start-workers:
	celery -A celery_app worker --concurrency=4

stop-workers:
	ps auxww | awk '/celery worker/ {print $2}' | xargs kill -9