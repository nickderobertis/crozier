

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_reaction_count_details_response import MessageReactionCountDetailsResponse
from .message_reaction_emoji_response import MessageReactionEmojiResponse


class MessageReactionResponse(UniversalBaseModel):
    emoji: MessageReactionEmojiResponse
    count: int
    count_details: MessageReactionCountDetailsResponse
    burst_colors: typing.List[str]
    me_burst: bool
    me: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
