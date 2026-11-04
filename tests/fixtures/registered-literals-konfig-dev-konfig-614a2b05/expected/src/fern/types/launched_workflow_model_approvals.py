

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .launched_workflow_model_approvals_state import LaunchedWorkflowModelApprovalsState


class LaunchedWorkflowModelApprovals(UniversalBaseModel):
    state: typing.Optional[LaunchedWorkflowModelApprovalsState] = pydantic.Field(default=None)
    """
    The state of the approvals.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
