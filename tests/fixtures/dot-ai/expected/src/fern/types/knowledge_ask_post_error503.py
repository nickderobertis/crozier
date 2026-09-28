

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .knowledge_ask_post_error503error import KnowledgeAskPostError503Error
from .knowledge_ask_post_error503meta import KnowledgeAskPostError503Meta


class KnowledgeAskPostError503(UniversalBaseModel):
    success: bool
    error: KnowledgeAskPostError503Error
    meta: typing.Optional[KnowledgeAskPostError503Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
