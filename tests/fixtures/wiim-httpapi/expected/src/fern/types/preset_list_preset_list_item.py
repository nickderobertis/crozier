

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PresetListPresetListItem(UniversalBaseModel):
    number: typing.Optional[int] = pydantic.Field(default=None)
    """
    Preset index (Start from 1)
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Playlist name
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Play url
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    Music source
    """

    picurl: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cover picture url
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
