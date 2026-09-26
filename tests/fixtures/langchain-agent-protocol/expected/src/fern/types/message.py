

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_content import MessageContent


class Message(UniversalBaseModel):
    role: str = pydantic.Field()
    """
    The role of the message.
    """

    content: MessageContent = pydantic.Field()
    """
    The content of the message.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the message.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The metadata of the message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
