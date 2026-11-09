

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateTranscriptionResponseJson(UniversalBaseModel):
    """
    Represents a transcription response returned by model, based on the provided input.
    """

    text: str = pydantic.Field()
    """
    The transcribed text.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
