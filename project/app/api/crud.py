# project/app/api/crud.py


from app.models.pydantic import PlayerPayloadSchema
from app.models.tortoise import Player

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
