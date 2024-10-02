from fastapi import APIRouter

from src.db import Session
from src.models.call import Call
from src.tasks.process_audio_file import process_audio_file

call_router = APIRouter()


@call_router.post("/call")
async def read_call(
    audio_url: str,
):
    session = Session()
    call = Call()
    session.add(call)
    session.commit()
    task = process_audio_file.delay(audio_url, call.id)
    return {"id": call.id, "task_id": task.id}


@call_router.get("/call/{call_id}")
async def read_call(call_id: int):
    session = Session()
    call = session.query(Call).get(call_id)
    return {
        "id": call.id,
        "name": call.name,
        "location": call.location,
        "emotional_tone": call.emotional_tone,
        "text": call.text,
        "categories": [category.title for category in call.categories]
    }
