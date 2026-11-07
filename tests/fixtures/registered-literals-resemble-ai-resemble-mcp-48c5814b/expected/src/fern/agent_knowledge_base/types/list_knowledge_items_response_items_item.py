

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_knowledge_items_response_items_item_source_type import ListKnowledgeItemsResponseItemsItemSourceType
from .list_knowledge_items_response_items_item_status import ListKnowledgeItemsResponseItemsItemStatus


class ListKnowledgeItemsResponseItemsItem(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    source_type: typing.Optional[ListKnowledgeItemsResponseItemsItemSourceType] = None
    status: typing.Optional[ListKnowledgeItemsResponseItemsItemStatus] = None
    error_message: typing.Optional[str] = None
    chunk_count: typing.Optional[int] = None
    url: typing.Optional[str] = None
    document_url: typing.Optional[str] = None
    document_filename: typing.Optional[str] = None
    agent_count: typing.Optional[int] = None
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
