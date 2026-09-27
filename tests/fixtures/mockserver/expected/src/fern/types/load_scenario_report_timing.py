

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LoadScenarioReportTiming(UniversalBaseModel):
    started_at_epoch_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="startedAtEpochMillis"), pydantic.Field(alias="startedAtEpochMillis")
    ] = None
    ended_at_epoch_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="endedAtEpochMillis"),
        pydantic.Field(alias="endedAtEpochMillis", description="epoch-millis the run ended; null while still running"),
    ] = None
    """
    epoch-millis the run ended; null while still running
    """

    duration_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="durationMillis"),
        pydantic.Field(alias="durationMillis", description="elapsed run time in milliseconds"),
    ] = None
    """
    elapsed run time in milliseconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
