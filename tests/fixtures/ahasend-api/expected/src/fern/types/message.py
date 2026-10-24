

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .message_content_parsed import MessageContentParsed
from .message_summary import MessageSummary


class Message(MessageSummary):
    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Original raw email content in RFC822 format. Omitted when message content is unavailable.
    """

    content_parsed: typing.Optional[MessageContentParsed] = pydantic.Field(default=None)
    """
    Parsed message content. Omitted when message content is unavailable.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
