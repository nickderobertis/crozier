

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dimension_sort_order import DimensionSortOrder


class Dimension(UniversalBaseModel):
    """
    A chart dimension. Dimensions are a structured label, class, or category for a set of measurements in your data.
    """

    column: typing.Optional[str] = pydantic.Field(default=None)
    """
    Required. The name of the column in the source SQL query that is used to chart the dimension.
    """

    column_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="columnType"),
        pydantic.Field(
            alias="columnType",
            description="Optional. The type of the dimension column. This is relevant only if one of the bin_size fields is set. If it is empty, the type TIMESTAMP or INT64 will be assumed based on which bin_size field is set. If populated, this should be set to one of the following types: DATE, TIME, DATETIME, TIMESTAMP, BIGNUMERIC, INT64, NUMERIC, FLOAT64.",
        ),
    ] = None
    """
    Optional. The type of the dimension column. This is relevant only if one of the bin_size fields is set. If it is empty, the type TIMESTAMP or INT64 will be assumed based on which bin_size field is set. If populated, this should be set to one of the following types: DATE, TIME, DATETIME, TIMESTAMP, BIGNUMERIC, INT64, NUMERIC, FLOAT64.
    """

    float_bin_size: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="floatBinSize"),
        pydantic.Field(
            alias="floatBinSize",
            description="Optional. float_bin_size is used when the column type used for a dimension is a floating point numeric column.",
        ),
    ] = None
    """
    Optional. float_bin_size is used when the column type used for a dimension is a floating point numeric column.
    """

    max_bin_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxBinCount"),
        pydantic.Field(
            alias="maxBinCount",
            description="A limit to the number of bins generated. When 0 is specified, the maximum count is not enforced.",
        ),
    ] = None
    """
    A limit to the number of bins generated. When 0 is specified, the maximum count is not enforced.
    """

    numeric_bin_size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numericBinSize"),
        pydantic.Field(
            alias="numericBinSize",
            description="numeric_bin_size is used when the column type used for a dimension is numeric or string.",
        ),
    ] = None
    """
    numeric_bin_size is used when the column type used for a dimension is numeric or string.
    """

    sort_column: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sortColumn"),
        pydantic.Field(
            alias="sortColumn",
            description="The column name to sort on for binning. This column can be the same column as this dimension or any other column used as a measure in the results. If sort_order is set to NONE, then this value is not used.",
        ),
    ] = None
    """
    The column name to sort on for binning. This column can be the same column as this dimension or any other column used as a measure in the results. If sort_order is set to NONE, then this value is not used.
    """

    sort_order: typing_extensions.Annotated[
        typing.Optional[DimensionSortOrder],
        FieldMetadata(alias="sortOrder"),
        pydantic.Field(alias="sortOrder", description="The sort order applied to the sort column."),
    ] = None
    """
    The sort order applied to the sort column.
    """

    time_bin_size: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="timeBinSize"),
        pydantic.Field(
            alias="timeBinSize",
            description="time_bin_size is used when the data type specified by column is a time type and the bin size is determined by a time duration. If column_type is DATE, this must be a whole value multiple of 1 day. If column_type is TIME, this must be less than or equal to 24 hours.",
        ),
    ] = None
    """
    time_bin_size is used when the data type specified by column is a time type and the bin size is determined by a time duration. If column_type is DATE, this must be a whole value multiple of 1 day. If column_type is TIME, this must be less than or equal to 24 hours.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
