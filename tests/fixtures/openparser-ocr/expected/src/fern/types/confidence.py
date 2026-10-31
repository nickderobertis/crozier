

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .confidence_scope import ConfidenceScope
from .confidence_source_scale import ConfidenceSourceScale


class Confidence(UniversalBaseModel):
    score: float
    scope: ConfidenceScope
    calibrated: bool
    source_value: typing.Optional[float] = None
    source_scale: typing.Optional[ConfidenceSourceScale] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
