

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_dto_activity_run import BuildSystemSharedDtoActivityRun
from .build_system_shared_dto_job_run_status import BuildSystemSharedDtoJobRunStatus
from .build_system_shared_dto_parameter_value import BuildSystemSharedDtoParameterValue


class BuildSystemSharedDtoJobRun(UniversalBaseModel):
    """
    A DTO for an IJobRun
    """

    activity_runs: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedDtoActivityRun]],
        FieldMetadata(alias="ActivityRuns"),
        pydantic.Field(alias="ActivityRuns", description="The activity runs belonging to this JobRun"),
    ] = None
    """
    The activity runs belonging to this JobRun
    """

    end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="EndDate"),
        pydantic.Field(alias="EndDate", description="The UTC date and time when the job completed"),
    ] = None
    """
    The UTC date and time when the job completed
    """

    job_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="JobID"),
        pydantic.Field(alias="JobID", description="The ID of the job that defines the run"),
    ] = None
    """
    The ID of the job that defines the run
    """

    job_run_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="JobRunID"),
        pydantic.Field(alias="JobRunID", description="The ID of this JobRun"),
    ] = None
    """
    The ID of this JobRun
    """

    parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedDtoParameterValue]],
        FieldMetadata(alias="Parameters"),
        pydantic.Field(alias="Parameters", description="The parameters used for this run of the job"),
    ] = None
    """
    The parameters used for this run of the job
    """

    start_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="StartDate"),
        pydantic.Field(alias="StartDate", description="The UTC date and time when the job started"),
    ] = None
    """
    The UTC date and time when the job started
    """

    status: typing_extensions.Annotated[
        typing.Optional[BuildSystemSharedDtoJobRunStatus],
        FieldMetadata(alias="Status"),
        pydantic.Field(alias="Status", description="The status of this JobRun"),
    ] = None
    """
    The status of this JobRun
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
