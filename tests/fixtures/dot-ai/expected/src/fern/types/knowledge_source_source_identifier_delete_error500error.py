

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .knowledge_source_source_identifier_delete_error500error_code import (
    KnowledgeSourceSourceIdentifierDeleteError500ErrorCode,
)


class KnowledgeSourceSourceIdentifierDeleteError500Error(UniversalBaseModel):
    code: KnowledgeSourceSourceIdentifierDeleteError500ErrorCode
    message: str
    details: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
