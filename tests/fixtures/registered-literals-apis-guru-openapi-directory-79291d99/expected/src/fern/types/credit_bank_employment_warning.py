

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_bank_employment_warning_type import CreditBankEmploymentWarningType
from .credit_bank_income_cause import CreditBankIncomeCause
from .credit_bank_income_warning_code import CreditBankIncomeWarningCode


class CreditBankEmploymentWarning(UniversalBaseModel):
    """
    The warning associated with the data that was unavailable for the Bank Employment Report.
    """

    cause: CreditBankIncomeCause
    warning_code: CreditBankIncomeWarningCode
    warning_type: CreditBankEmploymentWarningType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
