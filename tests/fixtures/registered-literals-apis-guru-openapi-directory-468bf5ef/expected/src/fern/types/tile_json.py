

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TileJson(UniversalBaseModel):
    """
    TileJSON model.
    Based on https://github.com/mapbox/tilejson-spec/tree/master/2.2.0
    """

    attribution: typing.Optional[str] = None
    bounds: typing.Optional[typing.List[float]] = None
    data: typing.Optional[typing.List[str]] = None
    description: typing.Optional[str] = None
    grids: typing.Optional[typing.List[str]] = None
    legend: typing.Optional[str] = None
    maxzoom: typing.Optional[int] = None
    minzoom: typing.Optional[int] = None
    name: typing.Optional[str] = None
    scheme: typing.Optional[str] = None
    template: typing.Optional[str] = None
    tilejson: typing.Optional[str] = None
    tiles: typing.List[str]
    version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
