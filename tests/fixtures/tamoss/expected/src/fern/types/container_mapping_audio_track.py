

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContainerMappingAudioTrack(UniversalBaseModel):
    """
    Mapping for channels in audio tracks to the Flow channels
    """

    channel_numbers: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array of (zero-based) container channel numbers in Flow order
    """

    channel_range: typing.Optional[str] = pydantic.Field(default=None)
    """
    Inclusive range of (zero-based) container channel numbers
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
