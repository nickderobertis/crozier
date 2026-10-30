

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .confidence import Confidence
from .formula_format import FormulaFormat
from .geometry import Geometry
from .source_provenance import SourceProvenance
from .text_span import TextSpan


class FormulaElement(UniversalBaseModel):
    id: str
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    value: str
    format: FormulaFormat
    spans: typing.List[TextSpan]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
