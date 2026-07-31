

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .media import Media


class VideoResponse(UniversalBaseModel):
    """
    Response model for video generation.
    """

    frames: typing.List[typing.List[Media]] = pydantic.Field()
    """
    The generated video frames.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
