

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .aggregation_function import AggregationFunction


class Measure(UniversalBaseModel):
    """
    A chart measure. Measures represent a measured property in your chart data such as rainfall in inches, number of units sold, revenue gained, etc.
    """

    aggregation_function: typing_extensions.Annotated[
        typing.Optional[AggregationFunction],
        FieldMetadata(alias="aggregationFunction"),
        pydantic.Field(
            alias="aggregationFunction",
            description='Required. The aggregation function applied to the input column. This must not be set to "none" unless binning is disabled on the dimension. The aggregation function is used to group points on the dimension bins.',
        ),
    ] = None
    """
    Required. The aggregation function applied to the input column. This must not be set to "none" unless binning is disabled on the dimension. The aggregation function is used to group points on the dimension bins.
    """

    column: typing.Optional[str] = pydantic.Field(default=None)
    """
    Required. The column name within in the dataset used for the measure.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
