

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .app import App
from .message_data_content import MessageDataContent
from .message_data_settings import MessageDataSettings
from .message_data_status import MessageDataStatus
from .user import User


class MessageData(UniversalBaseModel):
    app: typing.Optional[App] = None
    content: typing.Optional[MessageDataContent] = None
    id: int
    message: typing.Optional["Message"] = None
    owner: typing.Optional[User] = None
    settings: typing.Optional[MessageDataSettings] = None
    status: typing.Optional[MessageDataStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .conversation import Conversation
from .message import Message

update_forward_refs(MessageData, Conversation=Conversation, Message=Message)
