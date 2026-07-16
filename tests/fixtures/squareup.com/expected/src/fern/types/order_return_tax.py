

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class OrderReturnTax(UniversalBaseModel):
    """
    Represents a tax being returned that applies to one or more return line items in an order.

    Fixed-amount, order-scoped taxes are distributed across all non-zero return line item totals.
    The amount distributed to each return line item is relative to that item’s contribution to the
    order subtotal.
    """

    applied_money: typing.Optional[Money] = None
    catalog_object_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The catalog object ID referencing [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax).
    """

    catalog_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of the catalog object that this tax references.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tax's name.
    """

    percentage: typing.Optional[str] = pydantic.Field(default=None)
    """
    The percentage of the tax, as a string representation of a decimal number.
    For example, a value of `"7.25"` corresponds to a percentage of 7.25%.
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates the level at which the `OrderReturnTax` applies. For `ORDER` scoped
    taxes, Square generates references in `applied_taxes` on all
    `OrderReturnLineItem`s. For `LINE_ITEM` scoped taxes, the tax is only applied to
    `OrderReturnLineItem`s with references in their `applied_discounts` field.
    """

    source_tax_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tax `uid` from the order that contains the original tax charge.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates the calculation method used to apply the tax.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID that identifies the returned tax only within this order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
