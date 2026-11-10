

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_bank_income_item import CreditBankIncomeItem
from .credit_bank_income_summary import CreditBankIncomeSummary
from .credit_bank_income_warning import CreditBankIncomeWarning


class CreditBankIncome(UniversalBaseModel):
    """
    The report of the Bank Income data for an end user.
    """

    bank_income_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier associated with the Bank Income Report.
    """

    bank_income_summary: typing.Optional[CreditBankIncomeSummary] = None
    days_requested: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of days requested by the customer for the Bank Income Report.
    """

    generated_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when the Bank Income Report was generated.
    """

    items: typing.Optional[typing.List[CreditBankIncomeItem]] = pydantic.Field(default=None)
    """
    The list of Items in the report along with the associated metadata about the Item.
    """

    warnings: typing.Optional[typing.List[CreditBankIncomeWarning]] = pydantic.Field(default=None)
    """
    If data from the Bank Income report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
