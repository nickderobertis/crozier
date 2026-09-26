

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .documents_init200response_created_document import DocumentsInit200ResponseCreatedDocument
from .documents_init200response_created_upload import DocumentsInit200ResponseCreatedUpload


class DocumentsInit200ResponseCreated(UniversalBaseModel):
    document: DocumentsInit200ResponseCreatedDocument
    upload: DocumentsInit200ResponseCreatedUpload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
