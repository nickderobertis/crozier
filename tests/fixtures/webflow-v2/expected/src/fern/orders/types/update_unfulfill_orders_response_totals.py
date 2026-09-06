

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_unfulfill_orders_response_totals_extras_item import UpdateUnfulfillOrdersResponseTotalsExtrasItem
from .update_unfulfill_orders_response_totals_subtotal import UpdateUnfulfillOrdersResponseTotalsSubtotal
from .update_unfulfill_orders_response_totals_total import UpdateUnfulfillOrdersResponseTotalsTotal


class UpdateUnfulfillOrdersResponseTotals(UniversalBaseModel):
    """
    An object describing various pricing totals
    """

    subtotal: typing.Optional[UpdateUnfulfillOrdersResponseTotalsSubtotal] = pydantic.Field(default=None)
    """
    The subtotal price
    """

    extras: typing.Optional[typing.List[UpdateUnfulfillOrdersResponseTotalsExtrasItem]] = pydantic.Field(default=None)
    """
    An array of extra items, includes discounts, shipping, and taxes.
    """

    total: typing.Optional[UpdateUnfulfillOrdersResponseTotalsTotal] = pydantic.Field(default=None)
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
