

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .income_breakdown_type import IncomeBreakdownType


class IncomeBreakdown(UniversalBaseModel):
    """
    An object representing a breakdown of the different income types on the paystub.
    """

    hours: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number of hours logged for this income for this pay period.
    """

    rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The hourly rate at which the income is paid.
    """

    total: typing.Optional[float] = pydantic.Field(default=None)
    """
    The total pay for this pay period.
    """

    type: typing.Optional[IncomeBreakdownType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
