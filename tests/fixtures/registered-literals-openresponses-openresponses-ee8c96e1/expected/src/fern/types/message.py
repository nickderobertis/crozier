

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_content_item import MessageContentItem
from .message_role import MessageRole
from .message_status import MessageStatus


class Message(UniversalBaseModel):
    """
    A message to or from the model.
    """

    id: str = pydantic.Field()
    """
    The unique ID of the message.
    """

    status: MessageStatus = pydantic.Field()
    """
    The status of item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.
    """

    role: MessageRole = pydantic.Field()
    """
    The role of the message. One of `unknown`, `user`, `assistant`, `system`, `critic`, `discriminator`, `developer`, or `tool`.
    """

    content: typing.List[MessageContentItem] = pydantic.Field()
    """
    The content of the message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
