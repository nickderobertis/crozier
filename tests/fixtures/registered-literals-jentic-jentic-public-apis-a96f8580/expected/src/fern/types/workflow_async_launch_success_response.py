

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .launched_workflow_model import LaunchedWorkflowModel
from .workflow_async_launch_success_response_workflow_urls import WorkflowAsyncLaunchSuccessResponseWorkflowUrls
from .workflow_request_model import WorkflowRequestModel


class WorkflowAsyncLaunchSuccessResponse(UniversalBaseModel):
    """
    Response for a successfully asynchronously launched workflow.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    """

    request_payload: typing_extensions.Annotated[
        WorkflowRequestModel, FieldMetadata(alias="requestPayload"), pydantic.Field(alias="requestPayload")
    ]
    workflow_urls: typing_extensions.Annotated[
        typing.Optional[WorkflowAsyncLaunchSuccessResponseWorkflowUrls],
        FieldMetadata(alias="workflowUrls"),
        pydantic.Field(alias="workflowUrls", description=""),
    ] = None
    """
    
    """

    workflow: LaunchedWorkflowModel

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
