

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseServerThumbnailFormatsItem(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The file path component of the thumbnail format.
    """

    max_width: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum width of this format.
    """

    max_height: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum height of this format.
    """

    format: typing.Optional[str] = pydantic.Field(default=None)
    """
    The extension of this format.
    """

    animated: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this file format is animated. These formats
    are only generated for uploaded images which
    themselves are animated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
