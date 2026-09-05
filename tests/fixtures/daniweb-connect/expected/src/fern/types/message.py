

from __future__ import annotations

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .message_last_seen import MessageLastSeen
from .message_text import MessageText
from .user import User


class Message(UniversalBaseModel):
    author: typing.Optional[User] = None
    conversation: typing.Optional["Conversation"] = None
    id: int
    last_seen: typing.Optional[MessageLastSeen] = None
    text: typing.Optional[MessageText] = None
    timestamp: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .conversation import Conversation

update_forward_refs(Message, Conversation=Conversation)
