

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .confidence import Confidence
from .geometry import Geometry
from .text_span import TextSpan


class StructuredValue(UniversalBaseModel):
    text: str
    spans: typing.List[TextSpan]
    element_ids: typing.List[str]
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
