

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chunk import Chunk


class TextResponse(UniversalBaseModel):
    """
    Response model for text generation.
    """

    text: str = pydantic.Field()
    """
    The generated text.
    """

    chunks: typing.List[Chunk] = pydantic.Field()
    """
    The generated text chunks.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
