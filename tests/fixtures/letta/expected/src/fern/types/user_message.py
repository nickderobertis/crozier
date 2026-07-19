

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_message_content import UserMessageContent


class UserMessage(UniversalBaseModel):
    """
    A message sent by the user. Never streamed back on a response, only used for cursor pagination.

    Args:
        id (str): The ID of the message
        date (datetime): The date the message was created in ISO format
        name (Optional[str]): The name of the sender of the message
        content (Union[str, List[LettaUserMessageContentUnion]]): The message content sent by the user (can be a string or an array of multi-modal content parts)
    """

    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    seq_id: typing.Optional[int] = None
    run_id: typing.Optional[str] = None
    content: UserMessageContent = pydantic.Field()
    """
    The message content sent by the user (can be a string or an array of multi-modal content parts)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
