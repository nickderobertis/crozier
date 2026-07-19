

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ReasoningMessageListResult(UniversalBaseModel):
    """
    Reasoning message list result with agent context.

    Shape is identical to UpdateReasoningMessage but includes the owning agent_id and message id.
    """

    reasoning: str
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
