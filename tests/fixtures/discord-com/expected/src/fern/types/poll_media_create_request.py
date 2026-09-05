

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .poll_emoji_create_request import PollEmojiCreateRequest


class PollMediaCreateRequest(UniversalBaseModel):
    text: typing.Optional[str] = None
    emoji: typing.Optional[PollEmojiCreateRequest] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
