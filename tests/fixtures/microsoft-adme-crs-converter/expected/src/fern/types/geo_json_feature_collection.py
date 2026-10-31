

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .geo_json_feature_collection_geo_json_variant_internal import GeoJsonFeatureCollectionGeoJsonVariantInternal


class GeoJsonFeatureCollection(UniversalBaseModel):
    coordinate_reference_system_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CoordinateReferenceSystemID"),
        pydantic.Field(alias="CoordinateReferenceSystemID"),
    ] = None
    vertical_unit_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="VerticalUnitID"), pydantic.Field(alias="VerticalUnitID")
    ] = None
    bbox: typing.Optional[typing.List[float]] = None
    features: typing.Optional[typing.List["GeoJsonFeature"]] = None
    geo_json_variant_internal: typing_extensions.Annotated[
        typing.Optional[GeoJsonFeatureCollectionGeoJsonVariantInternal],
        FieldMetadata(alias="geoJsonVariantInternal"),
        pydantic.Field(alias="geoJsonVariantInternal"),
    ] = None
    persistable_reference_crs: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="persistableReferenceCrs"),
        pydantic.Field(alias="persistableReferenceCrs"),
    ] = None
    persistable_reference_unit_z: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="persistableReferenceUnitZ"),
        pydantic.Field(alias="persistableReferenceUnitZ"),
    ] = None
    properties: typing.Optional[typing.Dict[str, typing.Any]] = None
    type: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .geo_json_feature import GeoJsonFeature
from .geo_json_feature_geometry import GeoJsonFeatureGeometry

update_forward_refs(
    GeoJsonFeatureCollection, GeoJsonFeature=GeoJsonFeature, GeoJsonFeatureGeometry=GeoJsonFeatureGeometry
)
