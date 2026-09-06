

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_items_items_response_items_items_item import UpdateItemsItemsResponseItemsItemsItem
from .update_items_items_response_items_pagination import UpdateItemsItemsResponseItemsPagination


class UpdateItemsItemsResponseItems(UniversalBaseModel):
    """
    Results from collection items list
    """

    items: typing.Optional[typing.List[UpdateItemsItemsResponseItemsItemsItem]] = pydantic.Field(default=None)
    """
    List of Items within the collection
    """

    pagination: typing.Optional[UpdateItemsItemsResponseItemsPagination] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
