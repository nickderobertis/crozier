

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .refund_orders_response_totals_extras_item_price import RefundOrdersResponseTotalsExtrasItemPrice
from .refund_orders_response_totals_extras_item_type import RefundOrdersResponseTotalsExtrasItemType


class RefundOrdersResponseTotalsExtrasItem(UniversalBaseModel):
    """
    Extra order items, includes discounts, shipping, and taxes.
    """

    type: typing.Optional[RefundOrdersResponseTotalsExtrasItemType] = pydantic.Field(default=None)
    """
    The type of extra item this is.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable (but English) name for this extra charge.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable (but English) description of this extra charge.
    """

    price: typing.Optional[RefundOrdersResponseTotalsExtrasItemPrice] = pydantic.Field(default=None)
    """
    The price for the item
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
