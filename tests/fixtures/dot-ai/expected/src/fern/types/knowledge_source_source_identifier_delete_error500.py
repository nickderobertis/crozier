

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .knowledge_source_source_identifier_delete_error500error import KnowledgeSourceSourceIdentifierDeleteError500Error
from .knowledge_source_source_identifier_delete_error500meta import KnowledgeSourceSourceIdentifierDeleteError500Meta


class KnowledgeSourceSourceIdentifierDeleteError500(UniversalBaseModel):
    success: bool
    error: KnowledgeSourceSourceIdentifierDeleteError500Error
    meta: typing.Optional[KnowledgeSourceSourceIdentifierDeleteError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
