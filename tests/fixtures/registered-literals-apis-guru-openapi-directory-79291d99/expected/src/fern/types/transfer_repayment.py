

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransferRepayment(UniversalBaseModel):
    """
    A repayment is created automatically after one or more guaranteed transactions receive a return. If there are multiple eligible returns in a day, they are batched together into a single repayment.

    Repayments are sent over ACH, with funds typically available on the next banking day.
    """

    amount: str = pydantic.Field()
    """
    Decimal amount of the repayment as it appears on your account ledger.
    """

    created: dt.datetime = pydantic.Field()
    """
    The datetime when the repayment occurred, in RFC 3339 format.
    """

    iso_currency_code: str = pydantic.Field()
    """
    The currency of the repayment, e.g. "USD".
    """

    repayment_id: str = pydantic.Field()
    """
    Identifier of the repayment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
