

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_info import FileInfo
from .run_status import RunStatus
from .task_run_request import TaskRunRequest
from .task_run_response_output import TaskRunResponseOutput
from .task_run_response_run_type import TaskRunResponseRunType


class TaskRunResponse(UniversalBaseModel):
    run_id: str = pydantic.Field()
    """
    Unique identifier for this run. Run ID starts with `tsk_` for task runs and `wr_` for workflow runs.
    """

    status: RunStatus = pydantic.Field()
    """
    Current status of the run
    """

    output: typing.Optional[TaskRunResponseOutput] = pydantic.Field(default=None)
    """
    Output data from the run, if any. Format/schema depends on the data extracted by the run.
    """

    downloaded_files: typing.Optional[typing.List[FileInfo]] = pydantic.Field(default=None)
    """
    List of files downloaded during the run
    """

    recording_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to the recording of the run
    """

    screenshot_urls: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of last n screenshot URLs in reverse chronological order - the first one the list is the latest screenshot.
    """

    failure_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reason for failure if the run failed or terminated
    """

    created_at: dt.datetime = pydantic.Field()
    """
    Timestamp when this run was created
    """

    modified_at: dt.datetime = pydantic.Field()
    """
    Timestamp when this run was last modified
    """

    app_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to the application UI where the run can be viewed
    """

    run_type: TaskRunResponseRunType = pydantic.Field()
    """
    Types of a task run - task_v1, task_v2, openai_cua, anthropic_cua
    """

    run_request: typing.Optional[TaskRunRequest] = pydantic.Field(default=None)
    """
    The original request parameters used to start this task run
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
