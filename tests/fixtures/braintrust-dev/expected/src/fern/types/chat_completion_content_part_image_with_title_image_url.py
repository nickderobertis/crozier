

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_content_part_image_with_title_image_url_detail import (
    ChatCompletionContentPartImageWithTitleImageUrlDetail,
)


class ChatCompletionContentPartImageWithTitleImageUrl(UniversalBaseModel):
    url: str
    detail: typing.Optional[ChatCompletionContentPartImageWithTitleImageUrlDetail] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
