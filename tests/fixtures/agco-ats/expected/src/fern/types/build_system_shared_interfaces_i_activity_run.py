

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_interfaces_i_activity_run_status import BuildSystemSharedInterfacesIActivityRunStatus
from .build_system_shared_interfaces_i_activity_step import BuildSystemSharedInterfacesIActivityStep
from .build_system_shared_interfaces_i_parameter_value import BuildSystemSharedInterfacesIParameterValue


class BuildSystemSharedInterfacesIActivityRun(UniversalBaseModel):
    """
    IActivityRun
    """

    activity_run_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ActivityRunID"),
        pydantic.Field(alias="ActivityRunID", description="ActivityRunID"),
    ] = None
    """
    ActivityRunID
    """

    end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="EndDate"),
        pydantic.Field(alias="EndDate", description="EndDate"),
    ] = None
    """
    EndDate
    """

    job_activity_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="JobActivityID"),
        pydantic.Field(alias="JobActivityID", description="JobActivityID"),
    ] = None
    """
    JobActivityID
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
        pydantic.Field(alias="StartDate", description="StartDate"),
    ] = None
    """
    StartDate
    """

    status: typing_extensions.Annotated[
        typing.Optional[BuildSystemSharedInterfacesIActivityRunStatus],
        FieldMetadata(alias="Status"),
        pydantic.Field(alias="Status", description="Status"),
    ] = None
    """
    Status
    """

    steps: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedInterfacesIActivityStep]],
        FieldMetadata(alias="Steps"),
        pydantic.Field(alias="Steps", description="Steps"),
    ] = None
    """
    Steps
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
