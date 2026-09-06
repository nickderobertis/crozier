

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .c_store_query_result_metadata import CStoreQueryResultMetadata
from .store_item_id import StoreItemId


class CStoreQuerySearchSuggestionsResponse(UniversalBaseModel):
    ids: typing.Optional[typing.List[StoreItemId]] = None
    metadata: typing.Optional[CStoreQueryResultMetadata] = None
    store_items: typing.Optional[typing.List["StoreItem"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .store_item import StoreItem
from .store_item_included_items import StoreItemIncludedItems

update_forward_refs(
    CStoreQuerySearchSuggestionsResponse, StoreItem=StoreItem, StoreItemIncludedItems=StoreItemIncludedItems
)
