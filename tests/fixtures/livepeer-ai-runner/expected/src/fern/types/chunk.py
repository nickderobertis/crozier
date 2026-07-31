

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Chunk(UniversalBaseModel):
    """
    A chunk of text with a timestamp.
    """

    timestamp: typing.List[typing.Any] = pydantic.Field()
    """
    The timestamp of the chunk.
    """

    text: str = pydantic.Field()
    """
    The text of the chunk.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
