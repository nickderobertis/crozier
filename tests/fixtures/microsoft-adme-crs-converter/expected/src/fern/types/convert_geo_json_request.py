

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class ConvertGeoJsonRequest(UniversalBaseModel):
    feature_collection: typing_extensions.Annotated[
        typing.Optional["GeoJsonFeatureCollection"],
        FieldMetadata(alias="featureCollection"),
        pydantic.Field(alias="featureCollection"),
    ] = None
    to_crs: typing_extensions.Annotated[str, FieldMetadata(alias="toCRS"), pydantic.Field(alias="toCRS")]
    to_unit_z: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="toUnitZ"), pydantic.Field(alias="toUnitZ")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .geo_json_feature import GeoJsonFeature
from .geo_json_feature_collection import GeoJsonFeatureCollection
from .geo_json_feature_geometry import GeoJsonFeatureGeometry

update_forward_refs(
    ConvertGeoJsonRequest,
    GeoJsonFeature=GeoJsonFeature,
    GeoJsonFeatureCollection=GeoJsonFeatureCollection,
    GeoJsonFeatureGeometry=GeoJsonFeatureGeometry,
)
