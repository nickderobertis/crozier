

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .geo_json_base import GeoJsonBase


class GeoJsonMultiLineString(GeoJsonBase):
    coordinates: typing.Optional[typing.List[typing.List[typing.List[float]]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
