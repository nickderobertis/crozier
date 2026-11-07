

import typing

from ...types.workflow_async_in_progress_response import WorkflowAsyncInProgressResponse
from ...types.workflow_async_launch_failed_response import WorkflowAsyncLaunchFailedResponse
from ...types.workflow_async_launch_success_response import WorkflowAsyncLaunchSuccessResponse

RetrieveAsynchronousWorkflowStatusResponse = typing.Union[
    WorkflowAsyncLaunchSuccessResponse, WorkflowAsyncLaunchFailedResponse, WorkflowAsyncInProgressResponse
]
