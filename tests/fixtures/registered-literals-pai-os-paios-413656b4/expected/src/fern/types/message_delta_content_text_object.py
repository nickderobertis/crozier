

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_delta_content_text_object_text import MessageDeltaContentTextObjectText


class MessageDeltaContentTextObject(UniversalBaseModel):
    """
    The text content that is part of a message.
    """

    index: int = pydantic.Field()
    """
    The index of the content part in the message.
    """

    text: typing.Optional[MessageDeltaContentTextObjectText] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
