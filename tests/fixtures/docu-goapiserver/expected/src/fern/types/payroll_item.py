

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PayrollItem(UniversalBaseModel):
    """
    Payroll Item.
    """

    period: str
    regular: float
    overtime: float
    paid_time_off: float
    paid_holidays: float
    paid_sick: float
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
