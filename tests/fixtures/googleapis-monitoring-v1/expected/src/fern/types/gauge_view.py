

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GaugeView(UniversalBaseModel):
    """
    A gauge chart shows where the current value sits within a pre-defined range. The upper and lower bounds should define the possible range of values for the scorecard's query (inclusive).
    """

    lower_bound: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="lowerBound"),
        pydantic.Field(
            alias="lowerBound",
            description="The lower bound for this gauge chart. The value of the chart should always be greater than or equal to this.",
        ),
    ] = None
    """
    The lower bound for this gauge chart. The value of the chart should always be greater than or equal to this.
    """

    upper_bound: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="upperBound"),
        pydantic.Field(
            alias="upperBound",
            description="The upper bound for this gauge chart. The value of the chart should always be less than or equal to this.",
        ),
    ] = None
    """
    The upper bound for this gauge chart. The value of the chart should always be less than or equal to this.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
