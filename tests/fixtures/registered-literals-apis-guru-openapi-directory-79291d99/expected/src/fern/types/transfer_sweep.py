

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transfer_funding_account_id_response import TransferFundingAccountIdResponse


class TransferSweep(UniversalBaseModel):
    """
    Describes a sweep of funds to / from the sweep account.

    A sweep is associated with many sweep events (events of type `swept` or `return_swept`) which can be retrieved by invoking the `/transfer/event/list` endpoint with the corresponding `sweep_id`.

    `swept` events occur when the transfer amount is credited or debited from your sweep account, depending on the `type` of the transfer. `return_swept` events occur when a transfer is returned and Plaid undoes the credit or debit.

    The total sum of the `swept` and `return_swept` events is equal to the `amount` of the sweep Plaid creates and matches the amount of the entry on your sweep account ledger.
    """

    amount: str = pydantic.Field()
    """
    Signed decimal amount of the sweep as it appears on your sweep account ledger (e.g. "-10.00")
    
    If amount is not present, the sweep was net-settled to zero and outstanding debits and credits between the sweep account and Plaid are balanced.
    """

    created: dt.datetime = pydantic.Field()
    """
    The datetime when the sweep occurred, in RFC 3339 format.
    """

    funding_account_id: TransferFundingAccountIdResponse
    id: str = pydantic.Field()
    """
    Identifier of the sweep.
    """

    iso_currency_code: str = pydantic.Field()
    """
    The currency of the sweep, e.g. "USD".
    """

    settled: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date when the sweep settled, in the YYYY-MM-DD format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
