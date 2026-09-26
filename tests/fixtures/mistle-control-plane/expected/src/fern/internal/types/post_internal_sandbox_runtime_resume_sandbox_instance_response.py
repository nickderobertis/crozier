

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_resume_sandbox_instance_response_status import (
    PostInternalSandboxRuntimeResumeSandboxInstanceResponseStatus,
)


class PostInternalSandboxRuntimeResumeSandboxInstanceResponse(UniversalBaseModel):
    status: PostInternalSandboxRuntimeResumeSandboxInstanceResponseStatus
    sandbox_instance_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="sandboxInstanceId"), pydantic.Field(alias="sandboxInstanceId")
    ]
    workflow_run_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workflowRunId"), pydantic.Field(alias="workflowRunId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
