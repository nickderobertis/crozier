

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_content_part_text_with_title_cache_control import (
    ChatCompletionContentPartTextWithTitleCacheControl,
)


class ChatCompletionContentPartTextWithTitle(UniversalBaseModel):
    text: typing.Optional[str] = None
    cache_control: typing.Optional[ChatCompletionContentPartTextWithTitleCacheControl] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
