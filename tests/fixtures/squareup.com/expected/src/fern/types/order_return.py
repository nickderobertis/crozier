

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .order_money_amounts import OrderMoneyAmounts
from .order_return_discount import OrderReturnDiscount
from .order_return_line_item import OrderReturnLineItem
from .order_return_service_charge import OrderReturnServiceCharge
from .order_return_tax import OrderReturnTax
from .order_rounding_adjustment import OrderRoundingAdjustment


class OrderReturn(UniversalBaseModel):
    """
    The set of line items, service charges, taxes, discounts, tips, and other items being returned in an order.
    """

    return_amounts: typing.Optional[OrderMoneyAmounts] = None
    return_discounts: typing.Optional[typing.List[OrderReturnDiscount]] = pydantic.Field(default=None)
    """
    A collection of references to discounts being returned for an order, including the total
    applied discount amount to be returned. The discounts must reference a top-level discount ID
    from the source order.
    """

    return_line_items: typing.Optional[typing.List[OrderReturnLineItem]] = pydantic.Field(default=None)
    """
    A collection of line items that are being returned.
    """

    return_service_charges: typing.Optional[typing.List[OrderReturnServiceCharge]] = pydantic.Field(default=None)
    """
    A collection of service charges that are being returned.
    """

    return_taxes: typing.Optional[typing.List[OrderReturnTax]] = pydantic.Field(default=None)
    """
    A collection of references to taxes being returned for an order, including the total
    applied tax amount to be returned. The taxes must reference a top-level tax ID from the source
    order.
    """

    rounding_adjustment: typing.Optional[OrderRoundingAdjustment] = None
    source_order_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An order that contains the original sale of these return line items. This is unset
    for unlinked returns.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID that identifies the return only within this order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
