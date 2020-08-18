# project/app/models/pydantic.py


from pydantic import BaseModel


class PlayerPayloadSchema(BaseModel):
    name: str


class PlayerResponseSchema(PlayerPayloadSchema):
    id: int
