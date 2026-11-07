

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .redacted_audio_status import RedactedAudioStatus


class RedactedAudioResponse(UniversalBaseModel):
    status: RedactedAudioStatus = pydantic.Field()
    """
    The status of the redacted audio
    """

    redacted_audio_url: str = pydantic.Field()
    """
    The URL of the redacted audio file
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
