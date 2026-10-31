

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .confidence import Confidence
from .coordinate_unit import CoordinateUnit
from .document_page_quality import DocumentPageQuality
from .language import Language


class DocumentPage(UniversalBaseModel):
    number: int
    source_page_number: typing.Optional[int] = None
    width: float
    height: float
    unit: CoordinateUnit
    rotation_degrees: float
    languages: typing.List[Language]
    confidence: typing.Optional[Confidence] = None
    quality: typing.Optional[DocumentPageQuality] = None
    image_asset_id: typing.Optional[str] = None
    element_ids: typing.List[str]
    reading_order: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
