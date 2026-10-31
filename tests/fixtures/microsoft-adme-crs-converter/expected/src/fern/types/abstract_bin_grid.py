

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .abstract_spatial_location import AbstractSpatialLocation


class AbstractBinGrid(UniversalBaseModel):
    abcd_bin_grid_spatial_location: typing_extensions.Annotated[
        typing.Optional[AbstractSpatialLocation],
        FieldMetadata(alias="ABCDBinGridSpatialLocation"),
        pydantic.Field(alias="ABCDBinGridSpatialLocation"),
    ] = None
    bin_grid_definition_method_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="BinGridDefinitionMethodTypeID"),
        pydantic.Field(alias="BinGridDefinitionMethodTypeID"),
    ] = None
    bin_grid_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="BinGridName"), pydantic.Field(alias="BinGridName")
    ] = None
    bin_grid_type_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="BinGridTypeID"), pydantic.Field(alias="BinGridTypeID")
    ] = None
    coverage_percent: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="CoveragePercent"), pydantic.Field(alias="CoveragePercent")
    ] = None
    p6bin_grid_origin_easting: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="P6BinGridOriginEasting"),
        pydantic.Field(alias="P6BinGridOriginEasting"),
    ] = None
    p6bin_grid_origin_i: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="P6BinGridOriginI"), pydantic.Field(alias="P6BinGridOriginI")
    ] = None
    p6bin_grid_origin_j: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="P6BinGridOriginJ"), pydantic.Field(alias="P6BinGridOriginJ")
    ] = None
    p6bin_grid_origin_northing: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="P6BinGridOriginNorthing"),
        pydantic.Field(alias="P6BinGridOriginNorthing"),
    ] = None
    p6bin_node_increment_on_iaxis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="P6BinNodeIncrementOnIaxis"),
        pydantic.Field(alias="P6BinNodeIncrementOnIaxis"),
    ] = None
    p6bin_node_increment_on_jaxis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="P6BinNodeIncrementOnJaxis"),
        pydantic.Field(alias="P6BinNodeIncrementOnJaxis"),
    ] = None
    p6bin_width_on_iaxis: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="P6BinWidthOnIaxis"), pydantic.Field(alias="P6BinWidthOnIaxis")
    ] = None
    p6bin_width_on_jaxis: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="P6BinWidthOnJaxis"), pydantic.Field(alias="P6BinWidthOnJaxis")
    ] = None
    p6map_grid_bearing_of_bin_grid_jaxis: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="P6MapGridBearingOfBinGridJaxis"),
        pydantic.Field(alias="P6MapGridBearingOfBinGridJaxis"),
    ] = None
    p6scale_factor_of_bin_grid: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="P6ScaleFactorOfBinGrid"),
        pydantic.Field(alias="P6ScaleFactorOfBinGrid"),
    ] = None
    p6transformation_method: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="P6TransformationMethod"),
        pydantic.Field(alias="P6TransformationMethod"),
    ] = None
    source_bin_grid_app_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="SourceBinGridAppID"), pydantic.Field(alias="SourceBinGridAppID")
    ] = None
    source_bin_grid_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="SourceBinGridID"), pydantic.Field(alias="SourceBinGridID")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
