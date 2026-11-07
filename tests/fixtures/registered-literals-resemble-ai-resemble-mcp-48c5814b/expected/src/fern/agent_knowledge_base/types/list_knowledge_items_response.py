

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_knowledge_items_response_items_item import ListKnowledgeItemsResponseItemsItem
from .list_knowledge_items_response_pagination import ListKnowledgeItemsResponsePagination


class ListKnowledgeItemsResponse(UniversalBaseModel):
    success: typing.Optional[bool] = None
    items: typing.Optional[typing.List[ListKnowledgeItemsResponseItemsItem]] = None
    pagination: typing.Optional[ListKnowledgeItemsResponsePagination] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
