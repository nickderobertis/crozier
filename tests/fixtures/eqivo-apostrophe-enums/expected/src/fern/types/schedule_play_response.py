

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .schedule_play_response_message import SchedulePlayResponseMessage


class SchedulePlayResponse(UniversalBaseModel):
    message: typing_extensions.Annotated[
        SchedulePlayResponseMessage,
        FieldMetadata(alias="Message"),
        pydantic.Field(alias="Message", description="Response message"),
    ]
    """
    Response message
    """

    sched_play_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="SchedPlayId"),
        pydantic.Field(alias="SchedPlayId", description="Unique identifier of the scheduled playback request (UUIDv4)"),
    ]
    """
    Unique identifier of the scheduled playback request (UUIDv4)
    """

    success: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="Success"),
        pydantic.Field(alias="Success", description="Whether the request was successful or not"),
    ]
    """
    Whether the request was successful or not
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
