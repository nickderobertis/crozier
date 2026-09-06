

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_dto_activity_run_status_status import BuildSystemSharedDtoActivityRunStatusStatus


class BuildSystemSharedDtoActivityRunStatus(UniversalBaseModel):
    """
    A DTO for an IActivityRunStatus
    """

    current_step: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="CurrentStep"),
        pydantic.Field(
            alias="CurrentStep", description="The activity step currently executing, indicated by numeric order"
        ),
    ] = None
    """
    The activity step currently executing, indicated by numeric order
    """

    status: typing_extensions.Annotated[
        typing.Optional[BuildSystemSharedDtoActivityRunStatusStatus],
        FieldMetadata(alias="Status"),
        pydantic.Field(alias="Status", description="The status of the ActivityRun"),
    ] = None
    """
    The status of the ActivityRun
    """

    step_progress: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="StepProgress"),
        pydantic.Field(
            alias="StepProgress",
            description="The percent progress from the currently executing step.  This value shall be null if progress is not available",
        ),
    ] = None
    """
    The percent progress from the currently executing step.  This value shall be null if progress is not available
    """

    step_status: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StepStatus"),
        pydantic.Field(alias="StepStatus", description="The status text from the currently executing step"),
    ] = None
    """
    The status text from the currently executing step
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
