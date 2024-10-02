from celery import Celery

celery_app = Celery(
    'tasks',
    broker="redis://localhost:6379/0",
    backend="db+sqlite:///celery.db",
)

celery_app.conf.update(
    result_expires=3600,
)

if __name__ == "__main__":
    celery_app.start()
