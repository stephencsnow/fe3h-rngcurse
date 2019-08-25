from typing import List
from dataclasses import dataclass
import marshmallow_dataclass


@dataclass
class Stats:
    hp: int
    strength: int
    magic: int
    dexterity: int
    speed: int
    luck: int
    defense: int
    resistance: int
    charm: int


@dataclass
class Growths:
    hp: float
    strength: float
    magic: float
    dexterity: float
    speed: float
    luck: float
    defense: float
    resistance: float
    charm: float


@dataclass
class Character:
    name: str
    base: Stats
    growths: Growths


@dataclass
class CharacterClass:
    name: str
    base: Stats
    growths: Growths


@dataclass
class PlayerCharacterClass:
    character_class: CharacterClass
    level_ups: int


@dataclass
class PlayerCharacter:
    character: Character
    stats: Stats
    classes: List[PlayerCharacterClass]
    current_class: CharacterClass


@dataclass
class RequestCharacterClass:
    name: str
    level_ups: int
    is_current: bool


@dataclass
class RequestPlayerCharacter:
    character: str
    level: int
    stats: Stats
    classes: List[RequestCharacterClass]


PlayerCharacterSchema = marshmallow_dataclass.class_schema(PlayerCharacter)
InputSchema = marshmallow_dataclass.class_schema(RequestPlayerCharacter)
