

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .feature_geo_json_id import FeatureGeoJsonId
from .feature_geo_json_type import FeatureGeoJsonType
from .link import Link


class FeatureGeoJson(UniversalBaseModel):
    type: FeatureGeoJsonType
    geometry: "GeometryGeoJson"
    properties: typing.Optional[typing.Dict[str, typing.Any]] = None
    id: typing.Optional[FeatureGeoJsonId] = None
    links: typing.Optional[typing.List[Link]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .geometry_geo_json import GeometryGeoJson
from .geometrycollection_geo_json import GeometrycollectionGeoJson

update_forward_refs(
    FeatureGeoJson, GeometryGeoJson=GeometryGeoJson, GeometrycollectionGeoJson=GeometrycollectionGeoJson
)
