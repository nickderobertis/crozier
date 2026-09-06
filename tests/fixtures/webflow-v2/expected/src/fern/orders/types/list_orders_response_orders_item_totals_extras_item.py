

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_orders_response_orders_item_totals_extras_item_price import ListOrdersResponseOrdersItemTotalsExtrasItemPrice
from .list_orders_response_orders_item_totals_extras_item_type import ListOrdersResponseOrdersItemTotalsExtrasItemType


class ListOrdersResponseOrdersItemTotalsExtrasItem(UniversalBaseModel):
    """
    Extra order items, includes discounts, shipping, and taxes.
    """

    type: typing.Optional[ListOrdersResponseOrdersItemTotalsExtrasItemType] = pydantic.Field(default=None)
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

    price: typing.Optional[ListOrdersResponseOrdersItemTotalsExtrasItemPrice] = pydantic.Field(default=None)
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
