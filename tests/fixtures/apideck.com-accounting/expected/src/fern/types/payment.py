

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .created_by import CreatedBy
from .currency import Currency
from .currency_rate import CurrencyRate
from .downstream_id import DownstreamId
from .linked_customer import LinkedCustomer
from .linked_ledger_account import LinkedLedgerAccount
from .linked_supplier import LinkedSupplier
from .payment_allocations_item import PaymentAllocationsItem
from .payment_status import PaymentStatus
from .payment_type import PaymentType
from .row_version import RowVersion
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class Payment(UniversalBaseModel):
    account: typing.Optional[LinkedLedgerAccount] = None
    accounts_receivable_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the account to allocate payment to.
    """

    accounts_receivable_account_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of accounts receivable account.
    """

    allocations: typing.Optional[typing.List[PaymentAllocationsItem]] = None
    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    currency: typing.Optional[Currency] = None
    currency_rate: typing.Optional[CurrencyRate] = None
    customer: typing.Optional[LinkedCustomer] = None
    display_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Payment id to be displayed.
    """

    downstream_id: typing.Optional[DownstreamId] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier representing the entity
    """

    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional note to be associated with the payment.
    """

    payment_method: typing.Optional[str] = pydantic.Field(default=None)
    """
    Payment method name
    """

    payment_method_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the payment method.
    """

    payment_method_reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional reference message returned by payment method on processing
    """

    reconciled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Payment has been reconciled
    """

    reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional payment reference message ie: Debit remittance detail.
    """

    row_version: typing.Optional[RowVersion] = None
    status: typing.Optional[PaymentStatus] = pydantic.Field(default=None)
    """
    Status of payment
    """

    supplier: typing.Optional[LinkedSupplier] = None
    total_amount: float = pydantic.Field()
    """
    Amount of payment
    """

    transaction_date: dt.datetime = pydantic.Field()
    """
    Date transaction was entered - YYYY:MM::DDThh:mm:ss.sTZD
    """

    type: typing.Optional[PaymentType] = pydantic.Field(default=None)
    """
    Type of payment
    """

    updated_at: typing.Optional[UpdatedAt] = None
    updated_by: typing.Optional[UpdatedBy] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
