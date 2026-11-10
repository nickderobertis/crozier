

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_session_bank_employment_result import CreditSessionBankEmploymentResult
from .credit_session_bank_income_result import CreditSessionBankIncomeResult
from .credit_session_document_income_result import CreditSessionDocumentIncomeResult
from .credit_session_item_add_result import CreditSessionItemAddResult
from .credit_session_payroll_income_result import CreditSessionPayrollIncomeResult


class CreditSessionResults(UniversalBaseModel):
    """
    The set of results for a Link session.
    """

    bank_employment_results: typing.Optional[typing.List[CreditSessionBankEmploymentResult]] = pydantic.Field(
        default=None
    )
    """
    The set of bank employment verifications for the Link session.
    """

    bank_income_results: typing.Optional[typing.List[CreditSessionBankIncomeResult]] = pydantic.Field(default=None)
    """
    The set of bank income verifications for the Link session.
    """

    document_income_results: typing.Optional[CreditSessionDocumentIncomeResult] = None
    item_add_results: typing.Optional[typing.List[CreditSessionItemAddResult]] = pydantic.Field(default=None)
    """
    The set of Item adds for the Link session.
    """

    payroll_income_results: typing.Optional[typing.List[CreditSessionPayrollIncomeResult]] = pydantic.Field(
        default=None
    )
    """
    The set of payroll income verifications for the Link session.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
