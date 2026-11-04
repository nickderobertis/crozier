

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VideoRenderingResponse(UniversalBaseModel):
    message: typing.Optional[str] = None
    video_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the rendered MP4.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
