

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_attachment import MessageAttachment
from .message_content_part import MessageContentPart


class MessageContentParsed(UniversalBaseModel):
    parts: typing.List[MessageContentPart] = pydantic.Field()
    """
    Array of message content parts (text, HTML, etc.)
    """

    attachments: typing.List[MessageAttachment] = pydantic.Field()
    """
    Array of message attachments
    """

    headers: typing.Dict[str, typing.List[str]] = pydantic.Field()
    """
    Email headers as key-value pairs (values are arrays to handle multiple headers with same name)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
