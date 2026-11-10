

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document_analysis import DocumentAnalysis
from .document_status import DocumentStatus
from .physical_document_extracted_data import PhysicalDocumentExtractedData
from .physical_document_images import PhysicalDocumentImages
from .timestamp_nullable import TimestampNullable


class DocumentaryVerificationDocument(UniversalBaseModel):
    """
    Images, extracted data, and analysis from a user's identity document
    """

    analysis: DocumentAnalysis
    attempt: float = pydantic.Field()
    """
    The `attempt` field begins with 1 and increments with each subsequent document upload.
    """

    extracted_data: typing.Optional[PhysicalDocumentExtractedData] = None
    images: PhysicalDocumentImages
    redacted_at: typing.Optional[TimestampNullable] = None
    status: DocumentStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
