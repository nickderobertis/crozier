

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_interfaces_i_activity_run_status_status import (
    BuildSystemSharedInterfacesIActivityRunStatusStatus,
)


class BuildSystemSharedInterfacesIActivityRunStatus(UniversalBaseModel):
    """
    Declares members of objects that communicate the progress of an
                asynchronous activity run.
    """

    current_step: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="CurrentStep"),
        pydantic.Field(
            alias="CurrentStep", description="Gets or sets the number of the step the activity is currently running."
        ),
    ] = None
    """
    Gets or sets the number of the step the activity is currently running.
    """

    status: typing_extensions.Annotated[
        typing.Optional[BuildSystemSharedInterfacesIActivityRunStatusStatus],
        FieldMetadata(alias="Status"),
        pydantic.Field(alias="Status", description="Gets or sets the status of the activity run."),
    ] = None
    """
    Gets or sets the status of the activity run.
    """

    step_progress: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="StepProgress"),
        pydantic.Field(
            alias="StepProgress", description="Gets or sets a measurement of the current progress of the current step."
        ),
    ] = None
    """
    Gets or sets a measurement of the current progress of the current step.
    """

    step_status: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StepStatus"),
        pydantic.Field(
            alias="StepStatus",
            description="Gets or sets a description of the current status of the currently \r\n            running step.",
        ),
    ] = None
    """
    Gets or sets a description of the current status of the currently 
                running step.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
