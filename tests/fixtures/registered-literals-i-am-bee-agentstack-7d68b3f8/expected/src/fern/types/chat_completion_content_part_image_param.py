

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_url import ImageUrl


class ChatCompletionContentPartImageParam(UniversalBaseModel):
    """
    Learn about [image inputs](https://platform.openai.com/docs/guides/vision).
    """

    image_url: ImageUrl

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
