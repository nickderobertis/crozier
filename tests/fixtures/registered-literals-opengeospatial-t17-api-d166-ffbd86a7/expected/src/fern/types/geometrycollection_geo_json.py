

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class GeometrycollectionGeoJson(UniversalBaseModel):
    geometries: typing.List["GeometryGeoJson"]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .geometry_geo_json import GeometryGeoJson

update_forward_refs(GeometrycollectionGeoJson, GeometryGeoJson=GeometryGeoJson)
