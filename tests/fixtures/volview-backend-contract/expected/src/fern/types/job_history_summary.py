

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_history_summary_created_by import JobHistorySummaryCreatedBy
from .job_history_summary_output_summary import JobHistorySummaryOutputSummary
from .job_history_summary_result_state import JobHistorySummaryResultState
from .job_history_summary_state import JobHistorySummaryState


class JobHistorySummary(UniversalBaseModel):
    job_id: typing_extensions.Annotated[str, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    task_id: typing_extensions.Annotated[str, FieldMetadata(alias="taskId"), pydantic.Field(alias="taskId")]
    task_title: typing_extensions.Annotated[str, FieldMetadata(alias="taskTitle"), pydantic.Field(alias="taskTitle")]
    created_by: typing_extensions.Annotated[
        JobHistorySummaryCreatedBy, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    started_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ] = None
    finished_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="finishedAt"), pydantic.Field(alias="finishedAt")
    ] = None
    state: JobHistorySummaryState
    result_state: typing_extensions.Annotated[
        JobHistorySummaryResultState, FieldMetadata(alias="resultState"), pydantic.Field(alias="resultState")
    ]
    progress: typing.Optional[float] = None
    output_summary: typing_extensions.Annotated[
        typing.Optional[JobHistorySummaryOutputSummary],
        FieldMetadata(alias="outputSummary"),
        pydantic.Field(alias="outputSummary"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
