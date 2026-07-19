

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Base64Image(UniversalBaseModel):
    media_type: str = pydantic.Field()
    """
    The media type for the image.
    """

    data: str = pydantic.Field()
    """
    The base64 encoded image data.
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    What level of detail to use when processing and understanding the image (low, high, or auto to let the model decide)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
