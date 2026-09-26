

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .documents_init200response_created_document import DocumentsInit200ResponseCreatedDocument
from .documents_init200response_created_upload import DocumentsInit200ResponseCreatedUpload
from .documents_init200response_deduped_document import DocumentsInit200ResponseDedupedDocument
from .documents_init200response_resumed_document import DocumentsInit200ResponseResumedDocument
from .documents_init200response_resumed_upload import DocumentsInit200ResponseResumedUpload


class DocumentsInit200Response_Created(UniversalBaseModel):
    tag: typing.Literal["created"] = "created"
    document: DocumentsInit200ResponseCreatedDocument
    upload: DocumentsInit200ResponseCreatedUpload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentsInit200Response_Resumed(UniversalBaseModel):
    tag: typing.Literal["resumed"] = "resumed"
    document: DocumentsInit200ResponseResumedDocument
    upload: DocumentsInit200ResponseResumedUpload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentsInit200Response_Deduped(UniversalBaseModel):
    tag: typing.Literal["deduped"] = "deduped"
    document: DocumentsInit200ResponseDedupedDocument

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocumentsInit200Response = typing_extensions.Annotated[
    typing.Union[DocumentsInit200Response_Created, DocumentsInit200Response_Resumed, DocumentsInit200Response_Deduped],
    pydantic.Field(discriminator="tag"),
]
