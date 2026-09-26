

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .documents_init200response_resumed_document import DocumentsInit200ResponseResumedDocument
from .documents_init200response_resumed_upload import DocumentsInit200ResponseResumedUpload


class DocumentsInit200ResponseResumed(UniversalBaseModel):
    document: DocumentsInit200ResponseResumedDocument
    upload: DocumentsInit200ResponseResumedUpload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
