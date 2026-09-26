

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .knowledge_ask_post_response_data import KnowledgeAskPostResponseData
from .knowledge_ask_post_response_meta import KnowledgeAskPostResponseMeta


class KnowledgeAskPostResponse(UniversalBaseModel):
    success: bool
    data: KnowledgeAskPostResponseData
    meta: typing.Optional[KnowledgeAskPostResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
