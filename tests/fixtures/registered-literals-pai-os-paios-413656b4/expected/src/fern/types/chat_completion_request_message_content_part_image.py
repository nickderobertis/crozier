

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_request_message_content_part_image_image_url import (
    ChatCompletionRequestMessageContentPartImageImageUrl,
)


class ChatCompletionRequestMessageContentPartImage(UniversalBaseModel):
    image_url: ChatCompletionRequestMessageContentPartImageImageUrl

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
