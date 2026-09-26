

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1HourProjectEstimatedCost(UniversalBaseModel):
    fractional: typing.Optional[int] = None
    formatted: typing.Optional[str] = None
    amount: typing.Optional[float] = None
    currency_code: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
