

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_request_message_content_part_image_image_url import (
    ChatCompletionRequestMessageContentPartImageImageUrl,
)


class ChatCompletionRequestMessageContentPart_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionRequestMessageContentPart_ImageUrl(UniversalBaseModel):
    type: typing.Literal["image_url"] = "image_url"
    image_url: ChatCompletionRequestMessageContentPartImageImageUrl

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ChatCompletionRequestMessageContentPart = typing_extensions.Annotated[
    typing.Union[ChatCompletionRequestMessageContentPart_Text, ChatCompletionRequestMessageContentPart_ImageUrl],
    pydantic.Field(discriminator="type"),
]
