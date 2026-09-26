

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VideoVideo(UniversalBaseModel):
    url: str = pydantic.Field()
    """
    Publicly accessible URL of the video attachment. Supports file types .mp4 and .3gpp
    > Note: Only supports video codec H.264 and audio codec AAC
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
