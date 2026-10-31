

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lat_long import LatLong
from .osm_id import OsmId


class Place(UniversalBaseModel):
    country: typing.Optional[str] = None
    geohash: typing.Optional[str] = None
    google: typing.Optional[str] = None
    lat_long: typing_extensions.Annotated[
        typing.Optional[LatLong], FieldMetadata(alias="latLong"), pydantic.Field(alias="latLong")
    ] = None
    name: typing.Optional[str] = None
    osm: typing.Optional[OsmId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
