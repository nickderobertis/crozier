

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .aggregation_function import AggregationFunction
from .breakdown_sort_order import BreakdownSortOrder


class Breakdown(UniversalBaseModel):
    """
    Preview: A breakdown is an aggregation applied to the measures over a specified column. A breakdown can result in multiple series across a category for the provided measure. This is a preview feature and may be subject to change before final release.
    """

    aggregation_function: typing_extensions.Annotated[
        typing.Optional[AggregationFunction],
        FieldMetadata(alias="aggregationFunction"),
        pydantic.Field(
            alias="aggregationFunction",
            description="Required. The Aggregation function is applied across all data in each breakdown created.",
        ),
    ] = None
    """
    Required. The Aggregation function is applied across all data in each breakdown created.
    """

    column: typing.Optional[str] = pydantic.Field(default=None)
    """
    Required. The name of the column in the dataset containing the breakdown values.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Required. A limit to the number of breakdowns. If set to zero then all possible breakdowns are applied. The list of breakdowns is dependent on the value of the sort_order field.
    """

    sort_order: typing_extensions.Annotated[
        typing.Optional[BreakdownSortOrder],
        FieldMetadata(alias="sortOrder"),
        pydantic.Field(
            alias="sortOrder", description="Required. The sort order is applied to the values of the breakdown column."
        ),
    ] = None
    """
    Required. The sort order is applied to the values of the breakdown column.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
