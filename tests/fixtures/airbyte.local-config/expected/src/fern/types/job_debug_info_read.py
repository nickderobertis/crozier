

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attempt_info_read import AttemptInfoRead
from .job_debug_read import JobDebugRead
from .workflow_state_read import WorkflowStateRead


class JobDebugInfoRead(UniversalBaseModel):
    attempts: typing.List[AttemptInfoRead]
    job: JobDebugRead
    workflow_state: typing_extensions.Annotated[
        typing.Optional[WorkflowStateRead], FieldMetadata(alias="workflowState"), pydantic.Field(alias="workflowState")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
