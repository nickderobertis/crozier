

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .apr import Apr


class CreditCardLiability(UniversalBaseModel):
    """
    An object representing a credit card account.
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the account that this liability belongs to.
    """

    aprs: typing.List[Apr] = pydantic.Field()
    """
    The various interest rates that apply to the account. APR information is not provided by all card issuers; if APR data is not available, this array will be empty.
    """

    is_overdue: typing.Optional[bool] = pydantic.Field(default=None)
    """
    true if a payment is currently overdue. Availability for this field is limited.
    """

    last_payment_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount of the last payment.
    """

    last_payment_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). Availability for this field is limited.
    """

    last_statement_balance: typing.Optional[float] = pydantic.Field(default=None)
    """
    The total amount owed as of the last statement issued
    """

    last_statement_issue_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date of the last statement. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    """

    minimum_payment_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The minimum payment due for the next billing cycle.
    """

    next_payment_due_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The due date for the next payment. The due date is `null` if a payment is not expected. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
