

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_content_part_file_file import ChatCompletionContentPartFileFile
from .chat_completion_content_part_image_with_title_image_url import ChatCompletionContentPartImageWithTitleImageUrl
from .chat_completion_content_part_text_with_title_cache_control import (
    ChatCompletionContentPartTextWithTitleCacheControl,
)


class ChatCompletionContentPart_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    text: typing.Optional[str] = None
    cache_control: typing.Optional[ChatCompletionContentPartTextWithTitleCacheControl] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionContentPart_ImageUrl(UniversalBaseModel):
    type: typing.Literal["image_url"] = "image_url"
    image_url: ChatCompletionContentPartImageWithTitleImageUrl

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionContentPart_File(UniversalBaseModel):
    type: typing.Literal["file"] = "file"
    file: ChatCompletionContentPartFileFile

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ChatCompletionContentPart = typing_extensions.Annotated[
    typing.Union[ChatCompletionContentPart_Text, ChatCompletionContentPart_ImageUrl, ChatCompletionContentPart_File],
    pydantic.Field(discriminator="type"),
]
