

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .documents_init200response_created_upload_presigned_presigned_method import (
    DocumentsInit200ResponseCreatedUploadPresignedPresignedMethod,
)


class DocumentsInit200ResponseCreatedUploadPresignedPresigned(UniversalBaseModel):
    url: str
    headers: typing.Dict[str, str]
    method: DocumentsInit200ResponseCreatedUploadPresignedPresignedMethod
    expires_at: typing_extensions.Annotated[float, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
