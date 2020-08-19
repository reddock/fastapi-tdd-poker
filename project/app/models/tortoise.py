# project/app/models/tortoise.py


from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Player(models.Model):
    name = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = fields.TextField()
    location = fields.TextField()
    day_time = fields.DatetimeField()

    def __str__(self):
        return self.name


class Game(models.Model):
    name = fields.TextField()
    type = fields.TextField()
    event = fields.ForeignKeyField('models.Event', related_name="events", description="When the game takes place")

    def __str__(self):
        return self.name


PlayerSchema = pydantic_model_creator(Player)
EventSchema = pydantic_model_creator(Event)
