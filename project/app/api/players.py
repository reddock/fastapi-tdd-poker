# project/app/api/players.py


from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import PlayerPayloadSchema, PlayerResponseSchema
from app.models.tortoise import PlayerSchema

from typing import List


router = APIRouter()


@router.post("/", response_model=PlayerResponseSchema, status_code=201)
async def create_player(payload: PlayerPayloadSchema) -> PlayerResponseSchema:
    player_id = await crud.post(payload)

    response_object = {"id": player_id, "name": payload.name}
    return response_object


@router.get("/{id}/", response_model=PlayerSchema)
async def read_player(id: int) -> PlayerSchema:
    player = await crud.get(id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    return player


@router.get("/", response_model=List[PlayerSchema])
async def read_all_players() -> List[PlayerSchema]:
    return await crud.get_all()
