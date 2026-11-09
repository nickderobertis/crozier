

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .schedule_hangup_response_message import ScheduleHangupResponseMessage


class ScheduleHangupResponse(UniversalBaseModel):
    message: typing_extensions.Annotated[
        ScheduleHangupResponseMessage,
        FieldMetadata(alias="Message"),
        pydantic.Field(alias="Message", description="Response message"),
    ]
    """
    Response message
    """

    sched_hangup_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="SchedHangupId"),
        pydantic.Field(alias="SchedHangupId", description="Unique identifier of the scheduled hangup request (UUIDv4)"),
    ]
    """
    Unique identifier of the scheduled hangup request (UUIDv4)
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
