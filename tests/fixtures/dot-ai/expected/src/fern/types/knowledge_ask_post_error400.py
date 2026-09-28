

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .knowledge_ask_post_error400error import KnowledgeAskPostError400Error
from .knowledge_ask_post_error400meta import KnowledgeAskPostError400Meta


class KnowledgeAskPostError400(UniversalBaseModel):
    success: bool
    error: KnowledgeAskPostError400Error
    meta: typing.Optional[KnowledgeAskPostError400Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
