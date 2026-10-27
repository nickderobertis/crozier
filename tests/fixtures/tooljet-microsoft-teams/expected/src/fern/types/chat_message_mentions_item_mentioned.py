

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_message_mentions_item_mentioned_user import ChatMessageMentionsItemMentionedUser


class ChatMessageMentionsItemMentioned(UniversalBaseModel):
    user: typing.Optional[ChatMessageMentionsItemMentionedUser] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
