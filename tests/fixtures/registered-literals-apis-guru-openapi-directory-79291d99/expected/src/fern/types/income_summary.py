

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .employee_income_summary_field_string import EmployeeIncomeSummaryFieldString
from .employer_income_summary_field_string import EmployerIncomeSummaryFieldString
from .pay_frequency import PayFrequency
from .projected_income_summary_field_number import ProjectedIncomeSummaryFieldNumber
from .transaction_data import TransactionData
from .ytd_gross_income_summary_field_number import YtdGrossIncomeSummaryFieldNumber
from .ytd_net_income_summary_field_number import YtdNetIncomeSummaryFieldNumber


class IncomeSummary(UniversalBaseModel):
    """
    The verified fields from a paystub verification. All fields are provided as reported on the paystub.
    """

    employee_name: EmployeeIncomeSummaryFieldString
    employer_name: EmployerIncomeSummaryFieldString
    pay_frequency: typing.Optional[PayFrequency] = None
    projected_wage: ProjectedIncomeSummaryFieldNumber
    verified_transaction: typing.Optional[TransactionData] = None
    ytd_gross_income: YtdGrossIncomeSummaryFieldNumber
    ytd_net_income: YtdNetIncomeSummaryFieldNumber

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
