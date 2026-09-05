

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CustomAudio(UniversalBaseModel):
    """
    A custom audio in a playlist, which is a type of playlist item.
    """

    audio: typing.Optional[str] = pydantic.Field(default=None)
    """
    Audio url, which can be played directly.
    """

    audio_length_sec: typing.Optional[int] = pydantic.Field(default=None)
    """
    Audio length in seconds.
    """

    image: typing.Optional[str] = pydantic.Field(default=None)
    """
    High resolution image url of this custom audio.
    """

    pub_date_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    Published date (in milliseconds) of this custom audio.
    For now, it's the same as **added_at_ms** of this playlist item.
    """

    thumbnail: typing.Optional[str] = pydantic.Field(default=None)
    """
    Low resolution image url of this custom audio.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Custom audio title.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
