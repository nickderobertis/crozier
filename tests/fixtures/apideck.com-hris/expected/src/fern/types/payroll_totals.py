

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PayrollTotals(UniversalBaseModel):
    check_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The total check amount for the payroll.
    """

    company_debit: typing.Optional[float] = pydantic.Field(default=None)
    """
    The total company debit for the payroll.
    """

    employee_benefit_deductions: typing.Optional[float] = pydantic.Field(default=None)
    """
    The total amount of employee deducted benefits for the payroll.
    """

    employee_taxes: typing.Optional[float] = pydantic.Field(default=None)
    """
    The total amount of employee paid taxes for the payroll.
    """

    employer_benefit_contributions: typing.Optional[float] = pydantic.Field(default=None)
    """
    The total amount of company contributed benefits for the payroll.
    """

    employer_taxes: typing.Optional[float] = pydantic.Field(default=None)
    """
    The total amount of employer paid taxes for the payroll.
    """

    gross_pay: typing.Optional[float] = pydantic.Field(default=None)
    """
    The gross pay amount for the payroll.
    """

    net_pay: typing.Optional[float] = pydantic.Field(default=None)
    """
    The net pay amount for the payroll.
    """

    tax_debit: typing.Optional[float] = pydantic.Field(default=None)
    """
    The total tax debit for the payroll.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
