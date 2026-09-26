

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .currency import Currency
from .financial_metrics_period_unit import FinancialMetricsPeriodUnit


class FinancialMetrics(UniversalBaseModel):
    currency: typing.Optional[Currency] = None
    errors: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    If there are no errors, an empty array is returned.
    """

    metrics: typing.Optional[typing.List[typing.Any]] = None
    period_unit: typing_extensions.Annotated[
        typing.Optional[FinancialMetricsPeriodUnit],
        FieldMetadata(alias="periodUnit"),
        pydantic.Field(alias="periodUnit"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
