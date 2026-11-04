

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ProvisioningStatusResult(UniversalBaseModel):
    completed_steps: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="completedSteps"), pydantic.Field(alias="completedSteps")
    ] = None
    current_step_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="currentStepDescription"),
        pydantic.Field(alias="currentStepDescription"),
    ] = None
    is_ready: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isReady"), pydantic.Field(alias="isReady")
    ] = None
    operation_started_time_utc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="operationStartedTimeUtc"),
        pydantic.Field(alias="operationStartedTimeUtc"),
    ] = None
    total_steps: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalSteps"), pydantic.Field(alias="totalSteps")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
