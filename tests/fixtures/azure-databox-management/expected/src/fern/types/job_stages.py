

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_error_details import JobErrorDetails
from .job_stages_stage_name import JobStagesStageName
from .job_stages_stage_status import JobStagesStageStatus


class JobStages(UniversalBaseModel):
    """
    Job stages.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Display name of the job stage."),
    ] = None
    """
    Display name of the job stage.
    """

    error_details: typing_extensions.Annotated[
        typing.Optional[typing.List[JobErrorDetails]],
        FieldMetadata(alias="errorDetails"),
        pydantic.Field(alias="errorDetails", description="Error details for the stage."),
    ] = None
    """
    Error details for the stage.
    """

    job_stage_details: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="jobStageDetails"),
        pydantic.Field(alias="jobStageDetails", description="Job Stage Details"),
    ] = None
    """
    Job Stage Details
    """

    stage_name: typing_extensions.Annotated[
        typing.Optional[JobStagesStageName],
        FieldMetadata(alias="stageName"),
        pydantic.Field(alias="stageName", description="Name of the job stage."),
    ] = None
    """
    Name of the job stage.
    """

    stage_status: typing_extensions.Annotated[
        typing.Optional[JobStagesStageStatus],
        FieldMetadata(alias="stageStatus"),
        pydantic.Field(alias="stageStatus", description="Status of the job stage."),
    ] = None
    """
    Status of the job stage.
    """

    stage_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="stageTime"),
        pydantic.Field(alias="stageTime", description="Time for the job stage in UTC ISO 8601 format."),
    ] = None
    """
    Time for the job stage in UTC ISO 8601 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
