

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bill_line_item import BillLineItem
from .bill_status import BillStatus
from .created_at import CreatedAt
from .created_by import CreatedBy
from .currency import Currency
from .currency_rate import CurrencyRate
from .downstream_id import DownstreamId
from .id import Id
from .linked_ledger_account import LinkedLedgerAccount
from .linked_supplier import LinkedSupplier
from .row_version import RowVersion
from .tax_inclusive import TaxInclusive
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class Bill(UniversalBaseModel):
    balance: typing.Optional[float] = pydantic.Field(default=None)
    """
    Balance of bill due.
    """

    bill_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Date bill was issued - YYYY-MM-DD.
    """

    bill_number: typing.Optional[str] = None
    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    currency: typing.Optional[Currency] = None
    currency_rate: typing.Optional[CurrencyRate] = None
    deposit: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of deposit made to this bill.
    """

    downstream_id: typing.Optional[DownstreamId] = None
    due_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The due date is the date on which a payment is scheduled to be received by the supplier - YYYY-MM-DD.
    """

    id: typing.Optional[Id] = None
    ledger_account: typing.Optional[LinkedLedgerAccount] = None
    line_items: typing.Optional[typing.List[BillLineItem]] = None
    notes: typing.Optional[str] = None
    paid_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The paid date is the date on which a payment was sent to the supplier - YYYY-MM-DD.
    """

    po_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.
    """

    reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional bill reference.
    """

    row_version: typing.Optional[RowVersion] = None
    status: typing.Optional[BillStatus] = pydantic.Field(default=None)
    """
    Invoice status
    """

    sub_total: typing.Optional[float] = pydantic.Field(default=None)
    """
    Sub-total amount, normally before tax.
    """

    supplier: typing.Optional[LinkedSupplier] = None
    tax_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Applicable tax id/code override if tax is not supplied on a line item basis.
    """

    tax_inclusive: typing.Optional[TaxInclusive] = None
    terms: typing.Optional[str] = pydantic.Field(default=None)
    """
    Terms of payment.
    """

    total: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total amount of bill, including tax.
    """

    total_tax: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total tax amount applied to this bill.
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
