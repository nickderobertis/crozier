

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document_authenticity_match_code import DocumentAuthenticityMatchCode
from .image_quality import ImageQuality
from .physical_document_extracted_data_analysis import PhysicalDocumentExtractedDataAnalysis


class DocumentAnalysis(UniversalBaseModel):
    """
    High level descriptions of how the associated document was processed. If a document fails verification, the details in the `analysis` object should help clarify why the document was rejected.
    """

    authenticity: DocumentAuthenticityMatchCode
    extracted_data: typing.Optional[PhysicalDocumentExtractedDataAnalysis] = None
    image_quality: ImageQuality

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
