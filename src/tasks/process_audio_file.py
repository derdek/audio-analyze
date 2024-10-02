from dataclasses import dataclass
from typing import Optional

from ml_models.speach_recognition import speach_recognition
from ml_models.text_classificator import analyse_emotional_tone
from src.db import Session
from src.models.call import Call
from celery_app import celery_app


@dataclass
class Payload:
    name: str
    location: Optional[str]


def get_name_and_location(text: str, call_id: int):
    # TODO: Implement the logic to extract the name and location from the text
    name = f"Call {call_id}"
    location = None
    return Payload(name=name, location=location)


@celery_app.task(name="process_audio_file", retries=3)
def process_audio_file(audio_path: str, call_id: int):
    session = Session()
    call = session.query(Call).get(call_id)
    text = speach_recognition(audio_path)
    payload = get_name_and_location(call.text, call_id)
    call.name = payload.name
    call.location = payload.location
    call.text = text
    call.emotional_tone = analyse_emotional_tone(call.text)
    session.commit()
