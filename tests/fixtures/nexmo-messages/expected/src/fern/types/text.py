

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .text_message_type import TextMessageType


class Text(BaseMessageType):
    message_type: typing.Optional[TextMessageType] = pydantic.Field(default=None)
    """
    The type of message to send. You must provide `text` in this field
    """

    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
