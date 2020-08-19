# project/app/api/crud.py


from app.models.pydantic import PlayerPayloadSchema, EventPayloadSchema
from app.models.tortoise import Player, Event

from typing import Union, List


async def post(payload: PlayerPayloadSchema) -> int:
    player = Player(name=payload.name, summary="dummy",)
    await player.save()
    return player.id


async def get(id: int) -> Union[dict, None]:
    player = await Player.filter(id=id).first().values()
    if player:
        return player[0]
    return None


async def get_all() -> List:
    players = await Player.all().values()
    return players


async def post_event(payload: EventPayloadSchema) -> int:
    event = Event(name=payload.name, location=payload.location, day_time=payload.day_time)
    await event.save()
    return event.id
