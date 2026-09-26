

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PaymentAggregateMetrics(UniversalBaseModel):
    count: typing.Optional[int] = None
    sum_amount: typing.Optional[float] = None
    sum_total_amount: typing.Optional[float] = None
    sum_fee_amount: typing.Optional[float] = None
    avg_amount: typing.Optional[float] = None
    avg_total_amount: typing.Optional[float] = None
    avg_fee_amount: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
