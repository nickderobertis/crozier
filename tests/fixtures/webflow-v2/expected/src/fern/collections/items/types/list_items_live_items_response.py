

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_items_live_items_response_items_item import ListItemsLiveItemsResponseItemsItem
from .list_items_live_items_response_pagination import ListItemsLiveItemsResponsePagination


class ListItemsLiveItemsResponse(UniversalBaseModel):
    """
    Results from collection items list
    """

    items: typing.List[ListItemsLiveItemsResponseItemsItem] = pydantic.Field()
    """
    List of Items within the collection
    """

    pagination: ListItemsLiveItemsResponsePagination

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
