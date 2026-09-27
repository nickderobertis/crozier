

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payroll_earnings import PayrollEarnings


class PayrollEmployee(UniversalBaseModel):
    """
    Payroll Employee.
    """

    payroll_id: str = pydantic.Field()
    """
    Payroll id.
    """

    employee_id: str = pydantic.Field()
    """
    Employee id.
    """

    employee_first_name: str
    employee_last_name: str
    employee_name: str
    employee_type: str
    pay_period_start_date: str
    pay_period_end_date: str
    hours: PayrollEarnings
    amount: PayrollEarnings

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
