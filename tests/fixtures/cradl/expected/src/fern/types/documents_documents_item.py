

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .documents_documents_item_content_type import DocumentsDocumentsItemContentType
from .documents_documents_item_ground_truth_item import DocumentsDocumentsItemGroundTruthItem


class DocumentsDocumentsItem(UniversalBaseModel):
    updated_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedTime"), pydantic.Field(alias="updatedTime")
    ] = None
    content_md5: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentMD5"), pydantic.Field(alias="contentMD5")
    ] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    retention_in_days: typing_extensions.Annotated[
        int, FieldMetadata(alias="retentionInDays"), pydantic.Field(alias="retentionInDays")
    ]
    ocr_file_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ocrFileUrl"), pydantic.Field(alias="ocrFileUrl")
    ] = None
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    description: typing.Optional[str] = None
    agent_run_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="agentRunId"), pydantic.Field(alias="agentRunId")
    ] = None
    content: typing.Optional[str] = None
    ground_truth: typing_extensions.Annotated[
        typing.Optional[typing.List[DocumentsDocumentsItemGroundTruthItem]],
        FieldMetadata(alias="groundTruth"),
        pydantic.Field(alias="groundTruth"),
    ] = None
    consent_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="consentId"), pydantic.Field(alias="consentId")
    ] = None
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    name: typing.Optional[str] = None
    created_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="createdTime"), pydantic.Field(alias="createdTime")
    ]
    dataset_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="datasetId"), pydantic.Field(alias="datasetId")
    ] = None
    document_id: typing_extensions.Annotated[str, FieldMetadata(alias="documentId"), pydantic.Field(alias="documentId")]
    file_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fileUrl"), pydantic.Field(alias="fileUrl")
    ] = None
    content_type: typing_extensions.Annotated[
        typing.Optional[DocumentsDocumentsItemContentType],
        FieldMetadata(alias="contentType"),
        pydantic.Field(alias="contentType"),
    ] = None
    annotation_file_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="annotationFileUrl"), pydantic.Field(alias="annotationFileUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(DocumentsDocumentsItem)
