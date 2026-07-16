

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money
from .order_line_item_applied_discount import OrderLineItemAppliedDiscount
from .order_line_item_applied_tax import OrderLineItemAppliedTax
from .order_quantity_unit import OrderQuantityUnit
from .order_return_line_item_modifier import OrderReturnLineItemModifier


class OrderReturnLineItem(UniversalBaseModel):
    """
    The line item being returned in an order.
    """

    applied_discounts: typing.Optional[typing.List[OrderLineItemAppliedDiscount]] = pydantic.Field(default=None)
    """
    The list of references to `OrderReturnDiscount` entities applied to the return line item. Each
    `OrderLineItemAppliedDiscount` has a `discount_uid` that references the `uid` of a top-level
    `OrderReturnDiscount` applied to the return line item. On reads, the applied amount
    is populated.
    """

    applied_taxes: typing.Optional[typing.List[OrderLineItemAppliedTax]] = pydantic.Field(default=None)
    """
    The list of references to `OrderReturnTax` entities applied to the return line item. Each
    `OrderLineItemAppliedTax` has a `tax_uid` that references the `uid` of a top-level
    `OrderReturnTax` applied to the return line item. On reads, the applied amount
    is populated.
    """

    base_price_money: typing.Optional[Money] = None
    catalog_object_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) ID applied to this return line item.
    """

    catalog_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of the catalog object that this line item references.
    """

    gross_return_money: typing.Optional[Money] = None
    item_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of line item: an itemized return, a non-itemized return (custom amount),
    or the return of an unactivated gift card sale.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the line item.
    """

    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    The note of the return line item.
    """

    quantity: str = pydantic.Field()
    """
    The quantity returned, formatted as a decimal number.
    For example, `"3"`.
    
    Line items with a `quantity_unit` can have non-integer quantities.
    For example, `"1.70000"`.
    """

    quantity_unit: typing.Optional[OrderQuantityUnit] = None
    return_modifiers: typing.Optional[typing.List[OrderReturnLineItemModifier]] = pydantic.Field(default=None)
    """
    The [CatalogModifier](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifier)s applied to this line item.
    """

    source_line_item_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `uid` of the line item in the original sale order.
    """

    total_discount_money: typing.Optional[Money] = None
    total_money: typing.Optional[Money] = None
    total_tax_money: typing.Optional[Money] = None
    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID for this return line-item entry.
    """

    variation_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the variation applied to this return line item.
    """

    variation_total_price_money: typing.Optional[Money] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
