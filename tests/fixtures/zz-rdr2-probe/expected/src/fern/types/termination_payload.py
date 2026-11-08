

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TerminationPayload(UniversalBaseModel):
    type: str = pydantic.Field()
    """
    Indicates the session has been terminated.
    """

    audio_duration_seconds: int = pydantic.Field()
    """
    Duration of the audio in seconds.
    """

    session_duration_seconds: int = pydantic.Field()
    """
    Duration of the session in seconds.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
