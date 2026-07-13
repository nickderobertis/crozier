

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Image(UniversalBaseModel):
    attachment_public_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The public UUID of the public attachment containing the image.
    """

    content_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The content-type as a MIME filetype.
    """

    height: typing.Optional[int] = pydantic.Field(default=None)
    """
    The image height in pixels.
    """

    width: typing.Optional[int] = pydantic.Field(default=None)
    """
    The image width in pixels.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
