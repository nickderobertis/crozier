

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .send_chat_message_request_mentions_item_mentioned_user import SendChatMessageRequestMentionsItemMentionedUser


class SendChatMessageRequestMentionsItemMentioned(UniversalBaseModel):
    user: typing.Optional[SendChatMessageRequestMentionsItemMentionedUser] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
