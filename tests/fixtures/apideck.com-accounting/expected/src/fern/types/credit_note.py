

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .created_by import CreatedBy
from .credit_note_allocations_item import CreditNoteAllocationsItem
from .credit_note_status import CreditNoteStatus
from .credit_note_type import CreditNoteType
from .currency import Currency
from .currency_rate import CurrencyRate
from .invoice_line_item import InvoiceLineItem
from .linked_customer import LinkedCustomer
from .linked_ledger_account import LinkedLedgerAccount
from .row_version import RowVersion
from .tax_inclusive import TaxInclusive
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class CreditNote(UniversalBaseModel):
    account: typing.Optional[LinkedLedgerAccount] = None
    allocations: typing.Optional[typing.List[CreditNoteAllocationsItem]] = None
    balance: typing.Optional[float] = pydantic.Field(default=None)
    """
    The balance reflecting any payments made against the transaction.
    """

    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    currency: typing.Optional[Currency] = None
    currency_rate: typing.Optional[CurrencyRate] = None
    customer: typing.Optional[LinkedCustomer] = None
    date_issued: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD
    """

    date_paid: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier representing the entity
    """

    line_items: typing.Optional[typing.List[InvoiceLineItem]] = None
    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional note to be associated with the credit note.
    """

    number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Credit note number.
    """

    reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional reference message ie: Debit remittance detail.
    """

    remaining_credit: typing.Optional[float] = pydantic.Field(default=None)
    """
    Indicates the total credit amount still available to apply towards the payment.
    """

    row_version: typing.Optional[RowVersion] = None
    status: typing.Optional[CreditNoteStatus] = pydantic.Field(default=None)
    """
    Status of credit notes
    """

    sub_total: typing.Optional[float] = pydantic.Field(default=None)
    """
    Sub-total amount, normally before tax.
    """

    tax_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Applicable tax id/code override if tax is not supplied on a line item basis.
    """

    tax_inclusive: typing.Optional[TaxInclusive] = None
    terms: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional terms to be associated with the credit note.
    """

    total_amount: float = pydantic.Field()
    """
    Amount of transaction
    """

    total_tax: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total tax amount applied to this invoice.
    """

    type: typing.Optional[CreditNoteType] = pydantic.Field(default=None)
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
