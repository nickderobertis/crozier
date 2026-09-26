

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .documents_init200response_deduped_document import DocumentsInit200ResponseDedupedDocument


class DocumentsInit200ResponseDeduped(UniversalBaseModel):
    document: DocumentsInit200ResponseDedupedDocument

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
