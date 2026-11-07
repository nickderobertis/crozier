

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcript_ready_status import TranscriptReadyStatus


class TranscriptReadyNotification(UniversalBaseModel):
    """
    The notification when the transcript status is completed or error.
    """

    transcript_id: str = pydantic.Field()
    """
    The ID of the transcript
    """

    status: TranscriptReadyStatus = pydantic.Field()
    """
    The status of the transcript. Either completed or error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
