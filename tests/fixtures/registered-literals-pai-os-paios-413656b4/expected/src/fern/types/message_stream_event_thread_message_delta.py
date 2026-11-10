

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_delta_object import MessageDeltaObject


class MessageStreamEventThreadMessageDelta(UniversalBaseModel):
    """
    Occurs when parts of a [Message](/docs/api-reference/messages/object) are being streamed.
    """

    data: MessageDeltaObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
