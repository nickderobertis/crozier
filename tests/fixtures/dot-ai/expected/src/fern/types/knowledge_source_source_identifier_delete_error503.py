

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .knowledge_source_source_identifier_delete_error503error import KnowledgeSourceSourceIdentifierDeleteError503Error
from .knowledge_source_source_identifier_delete_error503meta import KnowledgeSourceSourceIdentifierDeleteError503Meta


class KnowledgeSourceSourceIdentifierDeleteError503(UniversalBaseModel):
    success: bool
    error: KnowledgeSourceSourceIdentifierDeleteError503Error
    meta: typing.Optional[KnowledgeSourceSourceIdentifierDeleteError503Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
