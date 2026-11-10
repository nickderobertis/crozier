

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_bank_income_category import CreditBankIncomeCategory
from .credit_bank_income_historical_summary import CreditBankIncomeHistoricalSummary
from .credit_bank_income_pay_frequency import CreditBankIncomePayFrequency


class CreditBankIncomeSource(UniversalBaseModel):
    """
    Detailed information for the income source.
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Plaid's unique identifier for the account.
    """

    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Maximum of all dates within the specific income sources in the user’s bank account for days requested by the client.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD).
    """

    historical_summary: typing.Optional[typing.List[CreditBankIncomeHistoricalSummary]] = None
    income_category: typing.Optional[CreditBankIncomeCategory] = None
    income_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The most common name or original description for the underlying income transactions.
    """

    income_source_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for an income source.
    """

    pay_frequency: typing.Optional[CreditBankIncomePayFrequency] = None
    start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Minimum of all dates within the specific income sources in the user's bank account for days requested by the client.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD).
    """

    total_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total amount of earnings in the user’s bank account for the specific income source for days requested by the client.
    """

    transaction_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of transactions for the income source within the start and end date.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
