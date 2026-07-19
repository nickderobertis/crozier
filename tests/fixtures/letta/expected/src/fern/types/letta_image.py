

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LettaImage(UniversalBaseModel):
    file_id: str = pydantic.Field()
    """
    The unique identifier of the image file persisted in storage.
    """

    media_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The media type for the image.
    """

    data: typing.Optional[str] = pydantic.Field(default=None)
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
