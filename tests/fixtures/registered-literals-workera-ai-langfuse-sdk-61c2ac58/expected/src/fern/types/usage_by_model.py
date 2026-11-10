

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UsageByModel(UniversalBaseModel):
    """
    Daily usage of a given model. Usage corresponds to the unit set for the specific model (e.g. tokens).
    """

    model: typing.Optional[str] = None
    input_usage: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="inputUsage"),
        pydantic.Field(alias="inputUsage", description="Total number of generation input units (e.g. tokens)"),
    ]
    """
    Total number of generation input units (e.g. tokens)
    """

    output_usage: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="outputUsage"),
        pydantic.Field(alias="outputUsage", description="Total number of generation output units (e.g. tokens)"),
    ]
    """
    Total number of generation output units (e.g. tokens)
    """

    total_usage: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalUsage"),
        pydantic.Field(alias="totalUsage", description="Total number of generation total units (e.g. tokens)"),
    ]
    """
    Total number of generation total units (e.g. tokens)
    """

    count_traces: typing_extensions.Annotated[
        int, FieldMetadata(alias="countTraces"), pydantic.Field(alias="countTraces")
    ]
    count_observations: typing_extensions.Annotated[
        int, FieldMetadata(alias="countObservations"), pydantic.Field(alias="countObservations")
    ]
    total_cost: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="totalCost"),
        pydantic.Field(alias="totalCost", description="Total model cost in USD"),
    ]
    """
    Total model cost in USD
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
