

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .input_image_content_detail import InputImageContentDetail


class InputImageContent(UniversalBaseModel):
    """
    An image input to the model. Learn about [image inputs](/docs/guides/vision).
    """

    image_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.
    """

    detail: InputImageContentDetail = pydantic.Field()
    """
    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
