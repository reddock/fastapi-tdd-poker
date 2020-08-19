# project/app/models/pydantic.py


from pydantic import BaseModel
from datetime import datetime


class PlayerPayloadSchema(BaseModel):
    name: str


class PlayerResponseSchema(PlayerPayloadSchema):
    id: int


class EventPayloadSchema(BaseModel):
    name: str
    location: str
    day_time: datetime


class EventResponseSchema(EventPayloadSchema):
    id: int
