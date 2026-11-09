

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_bank_income_cause import CreditBankIncomeCause
from .credit_bank_income_warning_code import CreditBankIncomeWarningCode
from .credit_bank_income_warning_type import CreditBankIncomeWarningType


class CreditBankIncomeWarning(UniversalBaseModel):
    """
    The warning associated with the data that was unavailable for the Bank Income Report.
    """

    cause: typing.Optional[CreditBankIncomeCause] = None
    warning_code: typing.Optional[CreditBankIncomeWarningCode] = None
    warning_type: typing.Optional[CreditBankIncomeWarningType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
