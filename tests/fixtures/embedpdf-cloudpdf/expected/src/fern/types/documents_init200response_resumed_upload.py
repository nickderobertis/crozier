

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .documents_init200response_resumed_upload_presigned_presigned import (
    DocumentsInit200ResponseResumedUploadPresignedPresigned,
)


class DocumentsInit200ResponseResumedUpload_Presigned(UniversalBaseModel):
    kind: typing.Literal["presigned"] = "presigned"
    presigned: DocumentsInit200ResponseResumedUploadPresignedPresigned
    key: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentsInit200ResponseResumedUpload_Proxy(UniversalBaseModel):
    kind: typing.Literal["proxy"] = "proxy"
    url: str
    key: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocumentsInit200ResponseResumedUpload = typing_extensions.Annotated[
    typing.Union[DocumentsInit200ResponseResumedUpload_Presigned, DocumentsInit200ResponseResumedUpload_Proxy],
    pydantic.Field(discriminator="kind"),
]
