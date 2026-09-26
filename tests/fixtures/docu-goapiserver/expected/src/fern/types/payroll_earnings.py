

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PayrollEarnings(UniversalBaseModel):
    """
    Payroll Earnings.
    """

    regular: float
    overtime: float
    paid_time_off: float
    paid_sick: float
    paid_holidays: float
    bonus: float
    other: float
    total: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
