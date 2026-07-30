

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .meta_destinations_list_response_items_item import MetaDestinationsListResponseItemsItem


class MetaDestinationsListResponse(UniversalBaseModel):
    items: typing.List[MetaDestinationsListResponseItemsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
