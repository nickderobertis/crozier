

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .confidence import Confidence
from .document_page_quality_defects_item import DocumentPageQualityDefectsItem
from .document_page_quality_metrics_item import DocumentPageQualityMetricsItem


class DocumentPageQuality(UniversalBaseModel):
    score: typing.Optional[Confidence] = None
    defects: typing.List[DocumentPageQualityDefectsItem]
    metrics: typing.List[DocumentPageQualityMetricsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
