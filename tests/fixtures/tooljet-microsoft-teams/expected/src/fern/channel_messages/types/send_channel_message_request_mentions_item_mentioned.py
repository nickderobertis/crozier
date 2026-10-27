

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .send_channel_message_request_mentions_item_mentioned_user import (
    SendChannelMessageRequestMentionsItemMentionedUser,
)


class SendChannelMessageRequestMentionsItemMentioned(UniversalBaseModel):
    user: typing.Optional[SendChannelMessageRequestMentionsItemMentionedUser] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
