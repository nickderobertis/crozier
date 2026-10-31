

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lineage_confidence_assertion_kind import LineageConfidenceAssertionKind
from .lineage_confidence_assertion_sources_item import LineageConfidenceAssertionSourcesItem
from .lineage_confidence_scale import LineageConfidenceScale


class LineageConfidenceAssertion(UniversalBaseModel):
    """
    A score with an explicit numeric scale, scope, granularity, calibration status, and provenance. Scores from different scopes or providers are not interchangeable probabilities.
    """

    score: float
    scale: LineageConfidenceScale
    kind: LineageConfidenceAssertionKind
    scope: str
    granularity: typing.Optional[str] = None
    calibrated: bool
    sources: typing.Optional[typing.List[LineageConfidenceAssertionSourcesItem]] = None
    method: typing.Optional[str] = None
    sample_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="sampleCount"), pydantic.Field(alias="sampleCount")
    ] = None
    attributes: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
