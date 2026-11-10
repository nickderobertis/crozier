

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .usage_by_model import UsageByModel


class DailyMetricsDetails(UniversalBaseModel):
    date: dt.date
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

    usage: typing.List[UsageByModel]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
