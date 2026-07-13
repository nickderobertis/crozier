

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DestinyConfigImagePyramidEntry(UniversalBaseModel):
    factor: typing.Optional[float] = pydantic.Field(default=None)
    """
    The factor by which the original image size has been reduced.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the subfolder where these images are located.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
