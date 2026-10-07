

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_attachment import ChatAttachment
from .chat_message_role import ChatMessageRole


class ChatMessage(UniversalBaseModel):
    """
    A message in a chat.
    """

    attachments: typing.Optional[typing.List[ChatAttachment]] = None
    content: typing.Any
    id: typing.Optional[str] = None
    metadata: typing.Optional[typing.Any] = None
    parts: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    role: ChatMessageRole

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
