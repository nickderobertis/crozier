

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChatResponse(UniversalBaseModel):
    """
    Response model for a posted Slack message.

    Immutable model returning the Slack API response fields.

    Attributes:
        ts: Message timestamp
        channel: Channel ID where the message was posted
        thread_ts: Thread timestamp if this was a threaded reply
    """

    channel: str = pydantic.Field()
    """
    Channel ID where the message was posted
    """

    thread_ts: typing.Optional[str] = pydantic.Field(default=None)
    """
    Thread timestamp if this was a threaded reply
    """

    ts: str = pydantic.Field()
    """
    Message timestamp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
