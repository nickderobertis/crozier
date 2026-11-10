

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_request_message_content_part_image_image_url_detail import (
    ChatCompletionRequestMessageContentPartImageImageUrlDetail,
)


class ChatCompletionRequestMessageContentPartImageImageUrl(UniversalBaseModel):
    url: str = pydantic.Field()
    """
    Either a URL of the image or the base64 encoded image data.
    """

    detail: typing.Optional[ChatCompletionRequestMessageContentPartImageImageUrlDetail] = pydantic.Field(default=None)
    """
    Specifies the detail level of the image. Learn more in the [Vision guide](/docs/guides/vision/low-or-high-fidelity-image-understanding).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
