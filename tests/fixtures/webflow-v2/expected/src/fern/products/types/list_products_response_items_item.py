

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_products_response_items_item_product import ListProductsResponseItemsItemProduct
from .list_products_response_items_item_skus_item import ListProductsResponseItemsItemSkusItem


class ListProductsResponseItemsItem(UniversalBaseModel):
    """
    A product and its SKUs.
    """

    product: typing.Optional[ListProductsResponseItemsItemProduct] = pydantic.Field(default=None)
    """
    The Product object
    """

    skus: typing.Optional[typing.List[ListProductsResponseItemsItemSkusItem]] = pydantic.Field(default=None)
    """
    A list of SKU Objects
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
