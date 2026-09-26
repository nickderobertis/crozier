

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .knowledge_ask_post_error500error import KnowledgeAskPostError500Error
from .knowledge_ask_post_error500meta import KnowledgeAskPostError500Meta


class KnowledgeAskPostError500(UniversalBaseModel):
    success: bool
    error: KnowledgeAskPostError500Error
    meta: typing.Optional[KnowledgeAskPostError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
