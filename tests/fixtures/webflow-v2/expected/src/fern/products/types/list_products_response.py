

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_products_response_items_item import ListProductsResponseItemsItem
from .list_products_response_pagination import ListProductsResponsePagination


class ListProductsResponse(UniversalBaseModel):
    """
    Results from product list
    """

    items: typing.Optional[typing.List[ListProductsResponseItemsItem]] = pydantic.Field(default=None)
    """
    List of Item objects within the Collection. Contains product and skus keys for each Item
    """

    pagination: typing.Optional[ListProductsResponsePagination] = pydantic.Field(default=None)
    """
    Pagination object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
