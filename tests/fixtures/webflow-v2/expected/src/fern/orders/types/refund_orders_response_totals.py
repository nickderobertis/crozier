

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .refund_orders_response_totals_extras_item import RefundOrdersResponseTotalsExtrasItem
from .refund_orders_response_totals_subtotal import RefundOrdersResponseTotalsSubtotal
from .refund_orders_response_totals_total import RefundOrdersResponseTotalsTotal


class RefundOrdersResponseTotals(UniversalBaseModel):
    """
    An object describing various pricing totals
    """

    subtotal: typing.Optional[RefundOrdersResponseTotalsSubtotal] = pydantic.Field(default=None)
    """
    The subtotal price
    """

    extras: typing.Optional[typing.List[RefundOrdersResponseTotalsExtrasItem]] = pydantic.Field(default=None)
    """
    An array of extra items, includes discounts, shipping, and taxes.
    """

    total: typing.Optional[RefundOrdersResponseTotalsTotal] = pydantic.Field(default=None)
    """
    The total price
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
