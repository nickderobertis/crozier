

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TowerLocation(UniversalBaseModel):
    c: typing.Optional[str] = pydantic.Field(default=None)
    """
    Country code
    """

    cid: typing.Optional[int] = pydantic.Field(default=None)
    """
    Cell ID
    """

    l: typing.Optional[str] = pydantic.Field(default=None)
    """
    Open Location Code
    """

    lac: typing.Optional[int] = pydantic.Field(default=None)
    """
    Location Area Code
    """

    lat: typing.Optional[float] = pydantic.Field(default=None)
    """
    Latitude
    """

    lon: typing.Optional[float] = pydantic.Field(default=None)
    """
    Longitude
    """

    mcc: typing.Optional[int] = pydantic.Field(default=None)
    """
    Mobile Country Code
    """

    mnc: typing.Optional[int] = pydantic.Field(default=None)
    """
    Mobile Network Code
    """

    n: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the location
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    The source of this location
    """

    time: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unix timestamp when this location was ascertained
    """

    towers: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of triangulation points
    """

    z: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timezone ID
    """

    zone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Timezone name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
