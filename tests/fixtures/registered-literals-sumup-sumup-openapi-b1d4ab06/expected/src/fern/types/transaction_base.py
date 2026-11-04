

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .currency import Currency
from .payment_type import PaymentType
from .transaction_status import TransactionStatus


class TransactionBase(UniversalBaseModel):
    """
    Core details shared by transaction resources.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of the transaction.
    """

    transaction_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Transaction code returned by the acquirer/processing entity after processing the transaction.
    """

    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total amount of the transaction.
    """

    currency: typing.Optional[Currency] = None
    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp of when the transaction was created.
    """

    status: typing.Optional[TransactionStatus] = None
    payment_type: typing.Optional[PaymentType] = None
    installments_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of installments for a deferred payment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
