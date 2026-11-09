

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entity_type import EntityType


class Entity(UniversalBaseModel):
    """
    A detected entity
    """

    entity_type: EntityType = pydantic.Field()
    """
    The type of entity for the detected entity
    """

    text: str = pydantic.Field()
    """
    The text for the detected entity
    """

    start: int = pydantic.Field()
    """
    The starting time, in milliseconds, at which the detected entity appears in the audio file
    """

    end: int = pydantic.Field()
    """
    The ending time, in milliseconds, for the detected entity in the audio file
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
