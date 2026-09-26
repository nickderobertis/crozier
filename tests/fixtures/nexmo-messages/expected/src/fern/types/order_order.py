

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .order_order_product_items_item import OrderOrderProductItemsItem


class OrderOrder(UniversalBaseModel):
    catalog_id: str = pydantic.Field()
    """
    The ID of the catalog containing the products in this order.
    """

    product_items: typing.List[OrderOrderProductItemsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
