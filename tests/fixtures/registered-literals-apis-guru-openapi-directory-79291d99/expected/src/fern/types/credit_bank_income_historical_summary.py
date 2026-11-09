

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_amount_with_currency import CreditAmountWithCurrency
from .credit_bank_income_transaction import CreditBankIncomeTransaction


class CreditBankIncomeHistoricalSummary(UniversalBaseModel):
    """
    The end user's monthly summary for the income source(s).
    """

    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The end date of the period included in this monthly summary.
    This date will be the last day of the month, unless the month being covered is a partial month because it is the last month included in the summary and the date range being requested does not end with the last day of the month.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD).
    """

    iso_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO 4217 currency code of the amount or balance.
    Please use [`total_amounts`](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-items-bank-income-sources-historical-summary-total-amounts) instead.
    """

    start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The start date of the period covered in this monthly summary.
    This date will be the first day of the month, unless the month being covered is a partial month because it is the first month included in the summary and the date range being requested does not begin with the first day of the month.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD).
    """

    total_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total amount of earnings for the income source(s) of the user for the month in the summary.
    This may return an incorrect value if the summary includes income sources in multiple currencies.
    Please use [`total_amounts`](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-items-bank-income-sources-historical-summary-total-amounts) instead.
    """

    total_amounts: typing.Optional[typing.List[CreditAmountWithCurrency]] = pydantic.Field(default=None)
    """
    Total amount of earnings for the income source(s) of the user for the month in the summary.
    This can contain multiple amounts, with each amount denominated in one unique currency.
    """

    transactions: typing.Optional[typing.List[CreditBankIncomeTransaction]] = None
    unofficial_currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unofficial currency code associated with the amount or balance. Always `null` if `iso_currency_code` is non-null.
    Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    Please use [`total_amounts`](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-items-bank-income-sources-historical-summary-total-amounts) instead.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
