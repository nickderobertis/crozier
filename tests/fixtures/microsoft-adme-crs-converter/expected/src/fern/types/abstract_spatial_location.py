

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .abstract_any_crs_feature_collection import AbstractAnyCrsFeatureCollection
from .abstract_feature_collection import AbstractFeatureCollection


class AbstractSpatialLocation(UniversalBaseModel):
    applied_operations: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="AppliedOperations"),
        pydantic.Field(alias="AppliedOperations"),
    ] = None
    as_ingested_coordinates: typing_extensions.Annotated[
        typing.Optional[AbstractAnyCrsFeatureCollection],
        FieldMetadata(alias="AsIngestedCoordinates"),
        pydantic.Field(alias="AsIngestedCoordinates"),
    ] = None
    coordinate_quality_check_date_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CoordinateQualityCheckDateTime"),
        pydantic.Field(alias="CoordinateQualityCheckDateTime"),
    ] = None
    coordinate_quality_check_performed_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CoordinateQualityCheckPerformedBy"),
        pydantic.Field(alias="CoordinateQualityCheckPerformedBy"),
    ] = None
    coordinate_quality_check_remarks: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="CoordinateQualityCheckRemarks"),
        pydantic.Field(alias="CoordinateQualityCheckRemarks"),
    ] = None
    qualitative_spatial_accuracy_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="QualitativeSpatialAccuracyTypeID"),
        pydantic.Field(alias="QualitativeSpatialAccuracyTypeID"),
    ] = None
    quantitative_accuracy_band_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="QuantitativeAccuracyBandID"),
        pydantic.Field(alias="QuantitativeAccuracyBandID"),
    ] = None
    spatial_geometry_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SpatialGeometryTypeID"),
        pydantic.Field(alias="SpatialGeometryTypeID"),
    ] = None
    spatial_location_coordinates_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SpatialLocationCoordinatesDate"),
        pydantic.Field(alias="SpatialLocationCoordinatesDate"),
    ] = None
    spatial_parameter_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SpatialParameterTypeID"),
        pydantic.Field(alias="SpatialParameterTypeID"),
    ] = None
    wgs84coordinates: typing_extensions.Annotated[
        typing.Optional[AbstractFeatureCollection],
        FieldMetadata(alias="Wgs84Coordinates"),
        pydantic.Field(alias="Wgs84Coordinates"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
