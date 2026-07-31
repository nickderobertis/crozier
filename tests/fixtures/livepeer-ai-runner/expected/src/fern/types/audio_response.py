

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .media_url import MediaUrl


class AudioResponse(UniversalBaseModel):
    """
    Response model for audio generation.
    """

    audio: MediaUrl = pydantic.Field()
    """
    The generated audio.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
