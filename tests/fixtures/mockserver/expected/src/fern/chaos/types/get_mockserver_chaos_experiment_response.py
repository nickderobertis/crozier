

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_mockserver_chaos_experiment_response_status import GetMockserverChaosExperimentResponseStatus


class GetMockserverChaosExperimentResponse(UniversalBaseModel):
    name: typing.Optional[str] = None
    status: typing.Optional[GetMockserverChaosExperimentResponseStatus] = None
    current_stage_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="currentStageIndex"), pydantic.Field(alias="currentStageIndex")
    ] = None
    total_stages: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalStages"), pydantic.Field(alias="totalStages")
    ] = None
    stage_elapsed_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="stageElapsedMillis"), pydantic.Field(alias="stageElapsedMillis")
    ] = None
    stage_remaining_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="stageRemainingMillis"), pydantic.Field(alias="stageRemainingMillis")
    ] = None
    loop_iteration: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="loopIteration"), pydantic.Field(alias="loopIteration")
    ] = None
    total_elapsed_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalElapsedMillis"), pydantic.Field(alias="totalElapsedMillis")
    ] = None
    experiment: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    the full experiment definition
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
