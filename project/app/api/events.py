# project/app/api/players.py


from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import EventPayloadSchema, EventResponseSchema
from app.models.tortoise import EventSchema

from typing import List


router = APIRouter()


@router.post("/", response_model=EventResponseSchema, status_code=201)
async def create_event(payload: EventPayloadSchema) -> EventResponseSchema:
    event_id = await crud.post_event(payload)

    response_object = {"id": event_id, "name": payload.name,
                       "location": payload.location, "day_time": payload.day_time}
    return response_object
