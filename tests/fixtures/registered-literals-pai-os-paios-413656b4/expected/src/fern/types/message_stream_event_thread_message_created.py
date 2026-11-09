

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_object import MessageObject


class MessageStreamEventThreadMessageCreated(UniversalBaseModel):
    """
    Occurs when a [message](/docs/api-reference/messages/object) is created.
    """

    data: MessageObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
