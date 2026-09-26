

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FamilyBalanceAggregateMetrics(UniversalBaseModel):
    count: typing.Optional[int] = None
    sum_balance: typing.Optional[float] = None
    avg_balance: typing.Optional[float] = None
    min_balance: typing.Optional[float] = None
    max_balance: typing.Optional[float] = None
    sum_positive_balance: typing.Optional[float] = None
    sum_negative_balance: typing.Optional[float] = None
    count_zero_balance: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
