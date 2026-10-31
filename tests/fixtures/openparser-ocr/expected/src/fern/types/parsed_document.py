

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document_asset import DocumentAsset
from .document_element import DocumentElement
from .document_page import DocumentPage
from .document_provenance import DocumentProvenance
from .document_relation import DocumentRelation
from .parsed_document_output_format import ParsedDocumentOutputFormat
from .text_annotation import TextAnnotation


class ParsedDocument(UniversalBaseModel):
    """
    Versioned OpenParser `openparser@1` document graph. `pages` establish coordinate spaces;
    `elements` carry semantic payloads and geometry; `relations` preserve hierarchy and
    cross-element meaning; `assets` hold reusable binary references (for example figure URIs).
    Compatible optional fields may be added within version 1; breaking representation changes
    create a new output-format version.
    """

    output_format: ParsedDocumentOutputFormat
    document_id: str
    provenance: DocumentProvenance
    text: str
    markdown: str = pydantic.Field()
    """
    Canonical best-effort Markdown rendering derived from the document graph.
    """

    pages: typing.List[DocumentPage] = pydantic.Field()
    """
    One-based contiguous page coordinate spaces with element membership and reading order.
    """

    elements: typing.List[DocumentElement] = pydantic.Field()
    """
    Ordered semantic nodes referenced by page membership, relations, and grounding citations.
    """

    text_annotations: typing.List[TextAnnotation]
    relations: typing.List[DocumentRelation]
    assets: typing.List[DocumentAsset]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
