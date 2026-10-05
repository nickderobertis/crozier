

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .open_shift_namespaces_task_result_actions_item import OpenShiftNamespacesTaskResultActionsItem
from .open_shift_namespaces_task_result_applied_actions_item import OpenShiftNamespacesTaskResultAppliedActionsItem
from .task_status import TaskStatus


class OpenShiftNamespacesTaskResult(UniversalBaseModel):
    """
    Result of a namespace reconciliation task.
    """

    actions: typing.Optional[typing.List[OpenShiftNamespacesTaskResultActionsItem]] = pydantic.Field(default=None)
    """
    All planned actions
    """

    applied_actions: typing.Optional[typing.List[OpenShiftNamespacesTaskResultAppliedActionsItem]] = pydantic.Field(
        default=None
    )
    """
    Actions that were applied (empty if dry_run)
    """

    applied_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of actions actually applied (0 if dry_run=True)
    """

    errors: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of errors encountered during reconciliation
    """

    status: TaskStatus = pydantic.Field()
    """
    Task execution status (pending/success/failed/skipped)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
