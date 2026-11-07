

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcript_status import TranscriptStatus


class TranscriptListItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The unique identifier for the transcript
    """

    resource_url: str = pydantic.Field()
    """
    The URL to retrieve the transcript
    """

    status: TranscriptStatus = pydantic.Field()
    """
    The status of the transcript
    """

    created: dt.datetime = pydantic.Field()
    """
    The date and time the transcript was created
    """

    completed: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the transcript was completed
    """

    audio_url: str = pydantic.Field()
    """
    The URL to the audio file
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message of why the transcript failed
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
