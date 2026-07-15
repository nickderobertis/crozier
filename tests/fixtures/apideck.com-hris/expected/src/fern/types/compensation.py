

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .benefit import Benefit
from .deduction import Deduction
from .id import Id
from .tax import Tax


class Compensation(UniversalBaseModel):
    benefits: typing.Optional[typing.List[Benefit]] = pydantic.Field(default=None)
    """
    An array of employee benefits for the pay period.
    """

    deductions: typing.Optional[typing.List[Deduction]] = pydantic.Field(default=None)
    """
    An array of employee deductions for the pay period.
    """

    employee_id: typing.Optional[Id] = None
    gross_pay: typing.Optional[float] = pydantic.Field(default=None)
    """
    The employee's gross pay. Only available when payroll has been processed
    """

    net_pay: typing.Optional[float] = pydantic.Field(default=None)
    """
    The employee's net pay. Only available when payroll has been processed
    """

    taxes: typing.Optional[typing.List[Tax]] = pydantic.Field(default=None)
    """
    An array of employer and employee taxes for the pay period.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
