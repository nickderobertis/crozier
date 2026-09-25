

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SendMessageRequestThreeTwoAudio(UniversalBaseModel):
    url: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The URL of the audio attachment.
    
    Only supports `.mp3` files
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
