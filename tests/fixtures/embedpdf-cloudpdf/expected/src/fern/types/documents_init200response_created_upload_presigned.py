

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .documents_init200response_created_upload_presigned_presigned import (
    DocumentsInit200ResponseCreatedUploadPresignedPresigned,
)


class DocumentsInit200ResponseCreatedUploadPresigned(UniversalBaseModel):
    presigned: DocumentsInit200ResponseCreatedUploadPresignedPresigned
    key: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
