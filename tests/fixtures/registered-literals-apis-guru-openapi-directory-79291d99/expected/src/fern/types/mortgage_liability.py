

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mortgage_interest_rate import MortgageInterestRate
from .mortgage_property_address import MortgagePropertyAddress


class MortgageLiability(UniversalBaseModel):
    """
    Contains details about a mortgage account.
    """

    account_id: str = pydantic.Field()
    """
    The ID of the account that this liability belongs to.
    """

    account_number: str = pydantic.Field()
    """
    The account number of the loan.
    """

    current_late_fee: typing.Optional[float] = pydantic.Field(default=None)
    """
    The current outstanding amount charged for late payment.
    """

    escrow_balance: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total amount held in escrow to pay taxes and insurance on behalf of the borrower.
    """

    has_pmi: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the borrower has private mortgage insurance in effect.
    """

    has_prepayment_penalty: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the borrower will pay a penalty for early payoff of mortgage.
    """

    interest_rate: MortgageInterestRate
    last_payment_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount of the last payment.
    """

    last_payment_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    """

    loan_term: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full duration of mortgage as at origination (e.g. `10 year`).
    """

    loan_type_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the type of loan, for example `conventional`, `fixed`, or `variable`. This field is provided directly from the loan servicer and does not have an enumerated set of possible values.
    """

    maturity_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Original date on which mortgage is due in full. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    """

    next_monthly_payment: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount of the next payment.
    """

    next_payment_due_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The due date for the next payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    """

    origination_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date on which the loan was initially lent. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    """

    origination_principal_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The original principal balance of the mortgage.
    """

    past_due_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of loan (principal + interest) past due for payment.
    """

    property_address: MortgagePropertyAddress
    ytd_interest_paid: typing.Optional[float] = pydantic.Field(default=None)
    """
    The year to date (YTD) interest paid.
    """

    ytd_principal_paid: typing.Optional[float] = pydantic.Field(default=None)
    """
    The YTD principal paid.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
