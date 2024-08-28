from datetime import date
from enum import Enum
from pydantic import BaseModel, validator


class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'


class GenreChoice(Enum):
    ROCK = 'Rock'
    ELECTRONIC = 'Electronic'
    METAL = 'Metal'
    HIP_HOP = 'Hip-Hop'


class Album(BaseModel):
    title: str
    release_date: date


class BandBase(BaseModel):
    name: str
    genre: GenreChoice
    albums: list[Album] = []


class BandCreate(BandBase):
    @validator('genre', pre=True)
    def title_case_genre(cls, value):
        return value.title()  # ROCK -> Rock


class BandWithID(BandBase):
    id: int
