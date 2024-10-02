from celery_app import celery_app
from src.tasks.process_audio_file import process_audio_file


if __name__ == "__main__":
    celery_app.start(argv=['worker', '--loglevel=INFO'])
