

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .active import Active
from .created_at import CreatedAt
from .created_by import CreatedBy
from .invoice_item_purchase_details import InvoiceItemPurchaseDetails
from .invoice_item_sales_details import InvoiceItemSalesDetails
from .invoice_item_type import InvoiceItemType
from .linked_ledger_account import LinkedLedgerAccount
from .quantity import Quantity
from .row_version import RowVersion
from .unit_price import UnitPrice
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class InvoiceItem(UniversalBaseModel):
    active: typing.Optional[Active] = None
    asset_account: typing.Optional[LinkedLedgerAccount] = None
    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    User defined item code
    """

    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A short description of the item
    """

    expense_account: typing.Optional[LinkedLedgerAccount] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the item.
    """

    income_account: typing.Optional[LinkedLedgerAccount] = None
    inventory_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date of opening balance if inventory item is tracked - YYYY-MM-DD.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Item name
    """

    purchase_details: typing.Optional[InvoiceItemPurchaseDetails] = None
    purchased: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Item is available for purchase transactions
    """

    quantity: typing.Optional[Quantity] = None
    row_version: typing.Optional[RowVersion] = None
    sales_details: typing.Optional[InvoiceItemSalesDetails] = None
    sold: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Item will be available on sales transactions
    """

    taxable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, transactions for this item are taxable
    """

    tracked: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Item is inventoried
    """

    type: typing.Optional[InvoiceItemType] = pydantic.Field(default=None)
    """
    Item type
    """

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
