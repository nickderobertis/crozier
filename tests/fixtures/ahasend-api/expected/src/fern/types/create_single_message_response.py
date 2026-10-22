

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_single_message_response_object import CreateSingleMessageResponseObject
from .create_single_message_response_recipient import CreateSingleMessageResponseRecipient
from .create_single_message_response_status import CreateSingleMessageResponseStatus
from .message_schedule import MessageSchedule


class CreateSingleMessageResponse(UniversalBaseModel):
    object: CreateSingleMessageResponseObject = pydantic.Field()
    """
    Object type identifier
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Message ID (null if the message was not sent)
    """

    recipient: CreateSingleMessageResponseRecipient
    status: CreateSingleMessageResponseStatus = pydantic.Field()
    """
    Status of the message
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message if the message was not sent
    """

    schedule: typing.Optional[MessageSchedule] = pydantic.Field(default=None)
    """
    Provided if the request contained a schedule
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
