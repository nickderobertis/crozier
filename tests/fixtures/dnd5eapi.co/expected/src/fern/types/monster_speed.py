

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MonsterSpeed(UniversalBaseModel):
    """
    Speed for a monster determines how fast it can move per turn.
    """

    burrow: typing.Optional[str] = pydantic.Field(default=None)
    """
    A monster that has a burrowing speed can use that speed to move through sand, earth, mud, or ice. A monster can’t burrow through solid rock unless it has a special trait that allows it to do so.
    """

    climb: typing.Optional[str] = pydantic.Field(default=None)
    """
    A monster that has a climbing speed can use all or part of its movement to move on vertical surfaces. The monster doesn’t need to spend extra movement to climb.
    """

    fly: typing.Optional[str] = pydantic.Field(default=None)
    """
    A monster that has a flying speed can use all or part of its movement to fly.
    """

    swim: typing.Optional[str] = pydantic.Field(default=None)
    """
    A monster that has a swimming speed doesn’t need to spend extra movement to swim.
    """

    walk: typing.Optional[str] = pydantic.Field(default=None)
    """
    All creatures have a walking speed, simply called the monster’s speed. Creatures that have no form of ground-based locomotion have a walking speed of 0 feet.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
