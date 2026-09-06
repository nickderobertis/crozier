

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_items_items_response_items_item import ListItemsItemsResponseItemsItem
from .list_items_items_response_pagination import ListItemsItemsResponsePagination


class ListItemsItemsResponse(UniversalBaseModel):
    """
    Results from collection items list
    """

    items: typing.List[ListItemsItemsResponseItemsItem] = pydantic.Field()
    """
    List of Items within the collection
    """

    pagination: ListItemsItemsResponsePagination

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
