

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .knowledge_source_source_identifier_delete_error503error_code import (
    KnowledgeSourceSourceIdentifierDeleteError503ErrorCode,
)


class KnowledgeSourceSourceIdentifierDeleteError503Error(UniversalBaseModel):
    code: KnowledgeSourceSourceIdentifierDeleteError503ErrorCode
    message: str
    details: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
