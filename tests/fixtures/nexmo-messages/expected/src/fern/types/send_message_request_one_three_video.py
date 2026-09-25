

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SendMessageRequestOneThreeVideo(UniversalBaseModel):
    caption: typing.Optional[str] = pydantic.Field(default=None)
    """
    Additional text to accompany the video file.
    """

    url: str = pydantic.Field()
    """
    The URL of the video attachment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
