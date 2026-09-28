

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .knowledge_ask_post_response_data_chunks_item import KnowledgeAskPostResponseDataChunksItem
from .knowledge_ask_post_response_data_sources_item import KnowledgeAskPostResponseDataSourcesItem


class KnowledgeAskPostResponseData(UniversalBaseModel):
    answer: str = pydantic.Field()
    """
    AI-synthesized answer to the question
    """

    sources: typing.List[KnowledgeAskPostResponseDataSourcesItem] = pydantic.Field()
    """
    Deduplicated source documents used
    """

    chunks: typing.List[KnowledgeAskPostResponseDataChunksItem] = pydantic.Field()
    """
    Original chunks for transparency
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
