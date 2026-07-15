

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .created_at import CreatedAt
from .created_by import CreatedBy
from .currency import Currency
from .currency_rate import CurrencyRate
from .downstream_id import DownstreamId
from .id import Id
from .invoice_line_item import InvoiceLineItem
from .invoice_status import InvoiceStatus
from .invoice_type import InvoiceType
from .linked_customer import LinkedCustomer
from .row_version import RowVersion
from .tax_inclusive import TaxInclusive
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class Invoice(UniversalBaseModel):
    balance: typing.Optional[float] = pydantic.Field(default=None)
    """
    Balance of invoice due.
    """

    billing_address: typing.Optional[Address] = None
    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    currency: typing.Optional[Currency] = None
    currency_rate: typing.Optional[CurrencyRate] = None
    customer: typing.Optional[LinkedCustomer] = None
    customer_memo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Customer memo
    """

    deposit: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of deposit made to this invoice.
    """

    discount_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Discount amount applied to this invoice.
    """

    discount_percentage: typing.Optional[float] = pydantic.Field(default=None)
    """
    Discount percentage applied to this invoice.
    """

    downstream_id: typing.Optional[DownstreamId] = None
    due_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD.
    """

    id: typing.Optional[Id] = None
    invoice_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Date invoice was issued - YYYY-MM-DD.
    """

    invoice_sent: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Invoice sent to contact/customer.
    """

    line_items: typing.Optional[typing.List[InvoiceLineItem]] = None
    number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Invoice number.
    """

    po_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.
    """

    reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional invoice reference.
    """

    row_version: typing.Optional[RowVersion] = None
    shipping_address: typing.Optional[Address] = None
    source_document_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero.
    """

    status: typing.Optional[InvoiceStatus] = pydantic.Field(default=None)
    """
    Invoice status
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
    template_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional invoice template
    """

    terms: typing.Optional[str] = pydantic.Field(default=None)
    """
    Terms of payment.
    """

    total: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total amount of invoice, including tax.
    """

    total_tax: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total tax amount applied to this invoice.
    """

    type: typing.Optional[InvoiceType] = pydantic.Field(default=None)
    """
    Invoice type
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
