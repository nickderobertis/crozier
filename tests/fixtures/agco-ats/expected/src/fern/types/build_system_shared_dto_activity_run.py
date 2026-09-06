

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_dto_activity_run_status import BuildSystemSharedDtoActivityRunStatus
from .build_system_shared_dto_activity_step import BuildSystemSharedDtoActivityStep
from .build_system_shared_dto_parameter_value import BuildSystemSharedDtoParameterValue


class BuildSystemSharedDtoActivityRun(UniversalBaseModel):
    """
    A DTO for an IActivityRun
    """

    activity_run_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ActivityRunID"),
        pydantic.Field(alias="ActivityRunID", description="The identifier for the ActivityRun"),
    ] = None
    """
    The identifier for the ActivityRun
    """

    end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="EndDate"),
        pydantic.Field(alias="EndDate", description="Read Only. The UTC date and time when the activity completed"),
    ] = None
    """
    Read Only. The UTC date and time when the activity completed
    """

    job_activity_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="JobActivityID"),
        pydantic.Field(
            alias="JobActivityID", description="Read Only. The ID of the Job Activity that defines this activity run"
        ),
    ] = None
    """
    Read Only. The ID of the Job Activity that defines this activity run
    """

    job_run_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="JobRunID"),
        pydantic.Field(
            alias="JobRunID", description="Read Only. The ID of the JobRun under which this ActivityRun is executing"
        ),
    ] = None
    """
    Read Only. The ID of the JobRun under which this ActivityRun is executing
    """

    parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedDtoParameterValue]],
        FieldMetadata(alias="Parameters"),
        pydantic.Field(
            alias="Parameters",
            description="The parameters used for this run of the activity.  Parameters cannot be added or removed, but output parameter values may be updated.",
        ),
    ] = None
    """
    The parameters used for this run of the activity.  Parameters cannot be added or removed, but output parameter values may be updated.
    """

    start_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="StartDate"),
        pydantic.Field(alias="StartDate", description="Read Only. The UTC date and time when the activity started"),
    ] = None
    """
    Read Only. The UTC date and time when the activity started
    """

    status: typing_extensions.Annotated[
        BuildSystemSharedDtoActivityRunStatus,
        FieldMetadata(alias="Status"),
        pydantic.Field(alias="Status", description="The status of this ActivityRun"),
    ]
    """
    The status of this ActivityRun
    """

    steps: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedDtoActivityStep]],
        FieldMetadata(alias="Steps"),
        pydantic.Field(
            alias="Steps",
            description="Read Only. The steps to be executed for the activity.  These steps come from the relationship through JobActivity down to ActivityStep",
        ),
    ] = None
    """
    Read Only. The steps to be executed for the activity.  These steps come from the relationship through JobActivity down to ActivityStep
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
