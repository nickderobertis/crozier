

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_items_live_items_response_items_item import UpdateItemsLiveItemsResponseItemsItem


class UpdateItemsLiveItemsResponse(UniversalBaseModel):
    """
    Results from collection items list
    """

    items: typing.Optional[typing.List[UpdateItemsLiveItemsResponseItemsItem]] = pydantic.Field(default=None)
    """
    List of Items within the collection
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
