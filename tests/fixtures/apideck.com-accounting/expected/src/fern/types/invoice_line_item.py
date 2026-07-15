

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .created_by import CreatedBy
from .id import Id
from .invoice_line_item_type import InvoiceLineItemType
from .linked_invoice_item import LinkedInvoiceItem
from .linked_ledger_account import LinkedLedgerAccount
from .linked_tax_rate import LinkedTaxRate
from .quantity import Quantity
from .row_version import RowVersion
from .unit_of_measure import UnitOfMeasure
from .unit_price import UnitPrice
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class InvoiceLineItem(UniversalBaseModel):
    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    User defined item code
    """

    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    department_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Department id
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    User defined description
    """

    discount_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Discount amount applied to the line item when supported downstream.
    """

    discount_percentage: typing.Optional[float] = pydantic.Field(default=None)
    """
    Discount percentage applied to the line item when supported downstream.
    """

    id: typing.Optional[Id] = None
    item: typing.Optional[LinkedInvoiceItem] = None
    ledger_account: typing.Optional[LinkedLedgerAccount] = None
    line_number: typing.Optional[int] = pydantic.Field(default=None)
    """
    Line number in the invoice
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Location id
    """

    quantity: typing.Optional[Quantity] = None
    row_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Row ID
    """

    row_version: typing.Optional[RowVersion] = None
    tax_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Tax amount
    """

    tax_rate: typing.Optional[LinkedTaxRate] = None
    total_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total amount of the line item
    """

    type: typing.Optional[InvoiceLineItemType] = pydantic.Field(default=None)
    """
    Item type
    """

    unit_of_measure: typing.Optional[UnitOfMeasure] = None
    unit_price: typing.Optional[UnitPrice] = None
    updated_at: typing.Optional[UpdatedAt] = None
    updated_by: typing.Optional[UpdatedBy] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
