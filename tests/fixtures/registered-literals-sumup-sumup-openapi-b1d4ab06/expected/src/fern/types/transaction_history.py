

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .card_type import CardType
from .transaction_base import TransactionBase
from .transaction_history_payout_type import TransactionHistoryPayoutType
from .transaction_history_type import TransactionHistoryType
from .transaction_id import TransactionId
from .transaction_mixin_history import TransactionMixinHistory


class TransactionHistory(TransactionBase, TransactionMixinHistory):
    """
    Transaction entry returned in history listing responses.
    """

    transaction_id: typing.Optional[TransactionId] = None
    client_transaction_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Client-supplied identifier of the transaction.
    """

    user: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address of the registered user (merchant) to whom the payment is made.
    """

    type: typing.Optional[TransactionHistoryType] = pydantic.Field(default=None)
    """
    Type of the transaction for the registered user specified in the `user` property.
    """

    card_type: typing.Optional[CardType] = None
    payout_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Payout date (if paid out at once).
    """

    payout_type: typing.Optional[TransactionHistoryPayoutType] = pydantic.Field(default=None)
    """
    Payout type.
    """

    refunded_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total refunded amount.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
