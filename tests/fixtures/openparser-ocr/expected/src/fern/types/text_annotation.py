

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .confidence import Confidence
from .language import Language
from .source_provenance import SourceProvenance
from .text_span import TextSpan
from .text_style import TextStyle


class TextAnnotation(UniversalBaseModel):
    id: str
    spans: typing.List[TextSpan]
    languages: typing.List[Language]
    style: typing.Optional[TextStyle] = None
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
