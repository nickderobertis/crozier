

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .slo_objective_result import SloObjectiveResult
from .slo_verdict_result import SloVerdictResult


class SloVerdict(UniversalBaseModel):
    """
    the overall verdict of an SLO evaluation (the AND of all objective results)
    """

    name: typing.Optional[str] = None
    result: typing.Optional[SloVerdictResult] = None
    window_from_epoch_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="windowFromEpochMillis"),
        pydantic.Field(alias="windowFromEpochMillis"),
    ] = None
    window_to_epoch_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="windowToEpochMillis"), pydantic.Field(alias="windowToEpochMillis")
    ] = None
    sample_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="sampleCount"), pydantic.Field(alias="sampleCount")
    ] = None
    objective_results: typing_extensions.Annotated[
        typing.Optional[typing.List[SloObjectiveResult]],
        FieldMetadata(alias="objectiveResults"),
        pydantic.Field(alias="objectiveResults"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
