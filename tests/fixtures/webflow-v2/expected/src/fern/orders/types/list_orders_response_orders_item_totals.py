

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_orders_response_orders_item_totals_extras_item import ListOrdersResponseOrdersItemTotalsExtrasItem
from .list_orders_response_orders_item_totals_subtotal import ListOrdersResponseOrdersItemTotalsSubtotal
from .list_orders_response_orders_item_totals_total import ListOrdersResponseOrdersItemTotalsTotal


class ListOrdersResponseOrdersItemTotals(UniversalBaseModel):
    """
    An object describing various pricing totals
    """

    subtotal: typing.Optional[ListOrdersResponseOrdersItemTotalsSubtotal] = pydantic.Field(default=None)
    """
    The subtotal price
    """

    extras: typing.Optional[typing.List[ListOrdersResponseOrdersItemTotalsExtrasItem]] = pydantic.Field(default=None)
    """
    An array of extra items, includes discounts, shipping, and taxes.
    """

    total: typing.Optional[ListOrdersResponseOrdersItemTotalsTotal] = pydantic.Field(default=None)
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
