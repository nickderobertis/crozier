

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_amount_with_currency import CreditAmountWithCurrency
from .credit_bank_income_historical_summary import CreditBankIncomeHistoricalSummary


class CreditBankIncomeSummary(UniversalBaseModel):
    """
    Summary for bank income across all income sources and items (max history of 730 days).
    """

    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The latest date in which all income sources identified by Plaid appear in the user's account.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD).
    """

    historical_summary: typing.Optional[typing.List[CreditBankIncomeHistoricalSummary]] = None
    income_categories_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of income categories per end user.
    """

    income_sources_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of income sources per end user.
    """

    income_transactions_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of income transactions per end user.
    """

    iso_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO 4217 currency code of the amount or balance.
    Please use [`total_amounts`](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts) instead.
    """

    start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The earliest date within the days requested in which all income sources identified by Plaid appear in a user's account.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD).
    """

    total_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total amount of earnings across all the income sources in the end user's Items for the days requested by the client.
    This may return an incorrect value if the summary includes income sources in multiple currencies.
    Please use [`total_amounts`](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts) instead.
    """

    total_amounts: typing.Optional[typing.List[CreditAmountWithCurrency]] = pydantic.Field(default=None)
    """
    Total amount of earnings across all the income sources in the end user's Items for the days requested by the client.
    This can contain multiple amounts, with each amount denominated in one unique currency.
    """

    unofficial_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unofficial currency code associated with the amount or balance. Always `null` if `iso_currency_code` is non-null.
    Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    Please use [`total_amounts`](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts) instead.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
