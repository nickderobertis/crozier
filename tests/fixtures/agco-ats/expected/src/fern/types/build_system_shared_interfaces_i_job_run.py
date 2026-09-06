

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_interfaces_i_activity_run import BuildSystemSharedInterfacesIActivityRun
from .build_system_shared_interfaces_i_job_run_status import BuildSystemSharedInterfacesIJobRunStatus
from .build_system_shared_interfaces_i_parameter_value import BuildSystemSharedInterfacesIParameterValue


class BuildSystemSharedInterfacesIJobRun(UniversalBaseModel):
    """
    interface of JobRun
    """

    activity_runs: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedInterfacesIActivityRun]],
        FieldMetadata(alias="ActivityRuns"),
        pydantic.Field(alias="ActivityRuns", description="ActivityRuns"),
    ] = None
    """
    ActivityRuns
    """

    end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="EndDate"),
        pydantic.Field(alias="EndDate", description="end date"),
    ] = None
    """
    end date
    """

    job_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="JobID"), pydantic.Field(alias="JobID", description="job id")
    ] = None
    """
    job id
    """

    job_run_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="JobRunID"), pydantic.Field(alias="JobRunID", description="JobRunID")
    ] = None
    """
    JobRunID
    """

    parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedInterfacesIParameterValue]],
        FieldMetadata(alias="Parameters"),
        pydantic.Field(alias="Parameters", description="Parameters"),
    ] = None
    """
    Parameters
    """

    start_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="StartDate"),
        pydantic.Field(alias="StartDate", description="Start Date"),
    ] = None
    """
    Start Date
    """

    status: typing_extensions.Annotated[
        typing.Optional[BuildSystemSharedInterfacesIJobRunStatus],
        FieldMetadata(alias="Status"),
        pydantic.Field(alias="Status", description="status"),
    ] = None
    """
    status
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
