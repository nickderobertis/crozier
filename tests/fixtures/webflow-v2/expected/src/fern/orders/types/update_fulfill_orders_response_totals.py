

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_fulfill_orders_response_totals_extras_item import UpdateFulfillOrdersResponseTotalsExtrasItem
from .update_fulfill_orders_response_totals_subtotal import UpdateFulfillOrdersResponseTotalsSubtotal
from .update_fulfill_orders_response_totals_total import UpdateFulfillOrdersResponseTotalsTotal


class UpdateFulfillOrdersResponseTotals(UniversalBaseModel):
    """
    An object describing various pricing totals
    """

    subtotal: typing.Optional[UpdateFulfillOrdersResponseTotalsSubtotal] = pydantic.Field(default=None)
    """
    The subtotal price
    """

    extras: typing.Optional[typing.List[UpdateFulfillOrdersResponseTotalsExtrasItem]] = pydantic.Field(default=None)
    """
    An array of extra items, includes discounts, shipping, and taxes.
    """

    total: typing.Optional[UpdateFulfillOrdersResponseTotalsTotal] = pydantic.Field(default=None)
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
