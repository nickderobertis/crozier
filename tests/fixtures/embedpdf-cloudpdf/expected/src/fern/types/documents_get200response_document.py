

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .documents_get200response_document_state import DocumentsGet200ResponseDocumentState
from .documents_get200response_document_thumbnail_state import DocumentsGet200ResponseDocumentThumbnailState


class DocumentsGet200ResponseDocument(UniversalBaseModel):
    id: str
    tenant_id: typing_extensions.Annotated[str, FieldMetadata(alias="tenantId"), pydantic.Field(alias="tenantId")]
    state: DocumentsGet200ResponseDocumentState
    base_sha: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="baseSha"), pydantic.Field(alias="baseSha")
    ] = None
    storage_size_bytes: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="storageSizeBytes"), pydantic.Field(alias="storageSizeBytes")
    ] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    idempotency_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="idempotencyKey"), pydantic.Field(alias="idempotencyKey")
    ] = None
    failure_reason: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="failureReason"), pydantic.Field(alias="failureReason")
    ] = None
    thumbnail_state: typing_extensions.Annotated[
        typing.Optional[DocumentsGet200ResponseDocumentThumbnailState],
        FieldMetadata(alias="thumbnailState"),
        pydantic.Field(alias="thumbnailState"),
    ] = None
    thumbnail_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="thumbnailUrl"), pydantic.Field(alias="thumbnailUrl")
    ] = None
    created_at: typing_extensions.Annotated[float, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[float, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]
    created_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
