

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_create_content import MessageCreateContent
from .message_create_role import MessageCreateRole
from .message_create_type import MessageCreateType


class MessageCreate(UniversalBaseModel):
    """
    Request to create a message
    """

    type: typing.Optional[MessageCreateType] = pydantic.Field(default=None)
    """
    The message type to be created.
    """

    role: MessageCreateRole = pydantic.Field()
    """
    The role of the participant.
    """

    content: MessageCreateContent = pydantic.Field()
    """
    The content of the message.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the participant.
    """

    otid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The offline threading id associated with this message
    """

    sender_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the sender of the message, can be an identity id or agent id
    """

    batch_item_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the LLMBatchItem that this message is associated with
    """

    group_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The multi-agent group that the message was sent in
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
