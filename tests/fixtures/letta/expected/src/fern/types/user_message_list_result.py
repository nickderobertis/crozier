

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_message_list_result_content import UserMessageListResultContent


class UserMessageListResult(UniversalBaseModel):
    """
    User message list result with agent context.

    Shape is identical to UpdateUserMessage but includes the owning agent_id and message id.
    """

    content: UserMessageListResultContent = pydantic.Field()
    """
    The message content sent by the user (can be a string or an array of multi-modal content parts)
    """

    message_id: str = pydantic.Field()
    """
    The unique identifier of the message.
    """

    agent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the agent that owns the message.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The time the message was created in ISO format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
