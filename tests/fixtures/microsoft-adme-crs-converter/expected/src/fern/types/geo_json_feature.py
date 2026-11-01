

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .geo_json_feature_geo_json_variant_internal import GeoJsonFeatureGeoJsonVariantInternal


class GeoJsonFeature(UniversalBaseModel):
    bbox: typing.Optional[typing.List[float]] = None
    geo_json_variant_internal: typing_extensions.Annotated[
        typing.Optional[GeoJsonFeatureGeoJsonVariantInternal],
        FieldMetadata(alias="geoJsonVariantInternal"),
        pydantic.Field(alias="geoJsonVariantInternal"),
    ] = None
    geometry: typing.Optional["GeoJsonFeatureGeometry"] = None
    properties: typing.Optional[typing.Dict[str, typing.Any]] = None
    type: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .geo_json_feature_collection import GeoJsonFeatureCollection
from .geo_json_feature_geometry import GeoJsonFeatureGeometry

update_forward_refs(
    GeoJsonFeature, GeoJsonFeatureCollection=GeoJsonFeatureCollection, GeoJsonFeatureGeometry=GeoJsonFeatureGeometry
)
