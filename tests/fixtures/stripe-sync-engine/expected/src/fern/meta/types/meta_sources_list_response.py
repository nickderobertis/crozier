

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .meta_sources_list_response_items_item import MetaSourcesListResponseItemsItem


class MetaSourcesListResponse(UniversalBaseModel):
    items: typing.List[MetaSourcesListResponseItemsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
