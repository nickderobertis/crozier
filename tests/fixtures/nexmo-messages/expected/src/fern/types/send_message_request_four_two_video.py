

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SendMessageRequestFourTwoVideo(UniversalBaseModel):
    caption: typing.Optional[str] = pydantic.Field(default=None)
    """
    Text caption to accompany message.
    """

    thumb_url: str = pydantic.Field()
    """
    URL to an image file for a thumbnail preview of the video.
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
