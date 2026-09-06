

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_reaction_emoji_response import MessageReactionEmojiResponse


class PollMediaResponse(UniversalBaseModel):
    text: typing.Optional[str] = None
    emoji: typing.Optional[MessageReactionEmojiResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
