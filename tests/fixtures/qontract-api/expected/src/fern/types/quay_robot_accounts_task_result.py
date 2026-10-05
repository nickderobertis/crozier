

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .quay_robot_accounts_task_result_actions_item import QuayRobotAccountsTaskResultActionsItem
from .quay_robot_accounts_task_result_applied_actions_item import QuayRobotAccountsTaskResultAppliedActionsItem
from .task_status import TaskStatus


class QuayRobotAccountsTaskResult(UniversalBaseModel):
    """
    Result model for a completed quay-robot-accounts reconciliation task.
    """

    actions: typing.Optional[typing.List[QuayRobotAccountsTaskResultActionsItem]] = pydantic.Field(default=None)
    """
    All actions calculated (desired - current), including any that failed to apply.
    """

    applied_actions: typing.Optional[typing.List[QuayRobotAccountsTaskResultAppliedActionsItem]] = pydantic.Field(
        default=None
    )
    """
    Actions that were successfully applied (non-dry-run only).
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
