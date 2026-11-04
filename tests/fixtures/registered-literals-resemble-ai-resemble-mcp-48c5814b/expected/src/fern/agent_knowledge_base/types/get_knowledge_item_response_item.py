

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_knowledge_item_response_item_agents_item import GetKnowledgeItemResponseItemAgentsItem
from .get_knowledge_item_response_item_source_type import GetKnowledgeItemResponseItemSourceType
from .get_knowledge_item_response_item_status import GetKnowledgeItemResponseItemStatus


class GetKnowledgeItemResponseItem(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    source_type: typing.Optional[GetKnowledgeItemResponseItemSourceType] = None
    status: typing.Optional[GetKnowledgeItemResponseItemStatus] = None
    error_message: typing.Optional[str] = None
    chunk_count: typing.Optional[int] = None
    url: typing.Optional[str] = None
    document_url: typing.Optional[str] = None
    document_filename: typing.Optional[str] = None
    agents: typing.Optional[typing.List[GetKnowledgeItemResponseItemAgentsItem]] = None
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
