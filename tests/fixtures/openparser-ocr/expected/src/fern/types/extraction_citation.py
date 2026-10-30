

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bounding_box import BoundingBox
from .confidence import Confidence
from .document_element_kind import DocumentElementKind
from .extraction_citation_granularity import ExtractionCitationGranularity
from .polygon import Polygon


class ExtractionCitation(UniversalBaseModel):
    """
    Verified provenance for one extracted leaf citation. Geometry comes from the parse graph element or table cell, never the model.
    """

    element_id: str
    table_cell_id: typing.Optional[str] = None
    page_number: int
    bbox: BoundingBox
    polygon: typing.Optional[Polygon] = None
    source_type: DocumentElementKind
    granularity: ExtractionCitationGranularity
    confidence: typing.Optional[Confidence] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
