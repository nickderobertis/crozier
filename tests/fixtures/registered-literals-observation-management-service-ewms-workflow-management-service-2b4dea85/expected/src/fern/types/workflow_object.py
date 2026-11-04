

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workflow_object_deactivated import WorkflowObjectDeactivated


class WorkflowObject(UniversalBaseModel):
    """
    Workflow object. See https://observation-management-service.github.io/ewms-docs/services/wms.html#workflow.
    """

    workflow_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier automatically generated for this workflow.
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    The epoch time when this workflow was created.
    """

    priority: typing.Optional[int] = pydantic.Field(default=None)
    """
    The workflow's priority level relative to other workflows.
    """

    deactivated: typing.Optional[WorkflowObjectDeactivated] = pydantic.Field(default=None)
    """
    Indicates why the workflow was deactivated.
    """

    deactivated_ts: typing.Optional[float] = pydantic.Field(default=None)
    """
    The epoch time when this workflow was deactivated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
