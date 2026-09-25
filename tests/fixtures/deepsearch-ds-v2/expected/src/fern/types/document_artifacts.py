

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document_artifacts_item import DocumentArtifactsItem
from .document_artifacts_page_item import DocumentArtifactsPageItem


class DocumentArtifacts(UniversalBaseModel):
    document_meta_json: typing.Optional[DocumentArtifactsItem] = None
    document_pdf: typing.Optional[DocumentArtifactsItem] = None
    document_json: typing.Optional[DocumentArtifactsItem] = None
    document_legacy_json: typing.Optional[DocumentArtifactsItem] = None
    document_md: typing.Optional[DocumentArtifactsItem] = None
    page_pdfs: typing.Optional[typing.List[DocumentArtifactsPageItem]] = None
    page_images: typing.Optional[typing.List[DocumentArtifactsPageItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
