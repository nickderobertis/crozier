

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InputVideoContent(UniversalBaseModel):
    """
    A content block representing a video input to the model.
    """

    video_url: str = pydantic.Field()
    """
    A base64 or remote url that resolves to a video file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
