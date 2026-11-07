

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .financial_payout_status import FinancialPayoutStatus
from .financial_payout_type import FinancialPayoutType


class FinancialPayout(UniversalBaseModel):
    """
    A single payout-related record.

    A record can represent either:
    - an actual payout sent to the merchant (`type = PAYOUT`)
    - a deduction applied against merchant funds for a refund, chargeback, direct debit return, or balance adjustment
    """

    id: int = pydantic.Field()
    """
    Unique identifier of the payout-related record.
    """

    type: FinancialPayoutType = pydantic.Field()
    """
    High-level payout record category.
    """

    amount: float = pydantic.Field()
    """
    Amount of the payout or deduction in major units.
    """

    date: dt.date = pydantic.Field()
    """
    Payout date associated with the record, in `YYYY-MM-DD` format.
    """

    currency: str = pydantic.Field()
    """
    Three-letter ISO 4217 currency code of the payout.
    """

    fee: float = pydantic.Field()
    """
    Fee amount associated with the payout record, in major units.
    """

    status: FinancialPayoutStatus = pydantic.Field()
    """
    Merchant-facing outcome of the payout record.
    """

    reference: str = pydantic.Field()
    """
    Processor or payout reference associated with the record.
    """

    transaction_code: str = pydantic.Field()
    """
    Transaction code of the original sale associated with the payout or deduction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
