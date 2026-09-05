

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .conversation_first_message import ConversationFirstMessage
from .user import User


class Conversation(UniversalBaseModel):
    first_message: typing.Optional[ConversationFirstMessage] = None
    id: int
    latest_message: typing.Optional["Message"] = None
    user_a: typing.Optional[User] = None
    user_b: typing.Optional[User] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .message import Message

update_forward_refs(Conversation, Message=Message)
