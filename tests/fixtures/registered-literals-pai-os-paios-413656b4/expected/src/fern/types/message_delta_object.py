

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_delta_object_delta import MessageDeltaObjectDelta
from .message_delta_object_object import MessageDeltaObjectObject


class MessageDeltaObject(UniversalBaseModel):
    """
    Represents a message delta i.e. any changed fields on a message during streaming.
    """

    id: str = pydantic.Field()
    """
    The identifier of the message, which can be referenced in API endpoints.
    """

    object: MessageDeltaObjectObject = pydantic.Field()
    """
    The object type, which is always `thread.message.delta`.
    """

    delta: MessageDeltaObjectDelta = pydantic.Field()
    """
    The delta containing the fields that have changed on the Message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
