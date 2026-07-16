

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class OrderReturnDiscount(UniversalBaseModel):
    """
    Represents a discount being returned that applies to one or more return line items in an
    order.

    Fixed-amount, order-scoped discounts are distributed across all non-zero return line item totals.
    The amount distributed to each return line item is relative to that item’s contribution to the
    order subtotal.
    """

    amount_money: typing.Optional[Money] = None
    applied_money: typing.Optional[Money] = None
    catalog_object_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The catalog object ID referencing [CatalogDiscount](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogDiscount).
    """

    catalog_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of the catalog object that this discount references.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The discount's name.
    """

    percentage: typing.Optional[str] = pydantic.Field(default=None)
    """
    The percentage of the tax, as a string representation of a decimal number.
    A value of `"7.25"` corresponds to a percentage of 7.25%.
    
    `percentage` is not set for amount-based discounts.
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates the level at which the `OrderReturnDiscount` applies. For `ORDER` scoped
    discounts, the server generates references in `applied_discounts` on all
    `OrderReturnLineItem`s. For `LINE_ITEM` scoped discounts, the discount is only applied to
    `OrderReturnLineItem`s with references in their `applied_discounts` field.
    """

    source_discount_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The discount `uid` from the order that contains the original application of this discount.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the discount. If it is created by the API, it is `FIXED_PERCENTAGE` or `FIXED_AMOUNT`.
    
    Discounts that do not reference a catalog object ID must have a type of
    `FIXED_PERCENTAGE` or `FIXED_AMOUNT`.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID that identifies the returned discount only within this order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
