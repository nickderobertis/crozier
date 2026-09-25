

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .custom_message_type import CustomMessageType


class Custom(BaseMessageType):
    custom: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    A custom payload, which is passed directly to WhatsApp for certain features such as templates and interactive messages. The schema of a custom object can vary widely. [Read more about Custom Objects](https://developer.vonage.com/messages/concepts/custom-objects).
    """

    message_type: typing.Optional[CustomMessageType] = pydantic.Field(default=None)
    """
    The type of message to send. You must provide `custom` in this field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
