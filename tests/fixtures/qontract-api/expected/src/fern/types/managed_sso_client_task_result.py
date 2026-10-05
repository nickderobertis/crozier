

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .managed_sso_client_task_result_actions_item import ManagedSsoClientTaskResultActionsItem
from .managed_sso_client_task_result_applied_actions_item import ManagedSsoClientTaskResultAppliedActionsItem
from .task_status import TaskStatus


class ManagedSsoClientTaskResult(UniversalBaseModel):
    """
    Result model for a completed managed-sso-client reconciliation task.
    """

    actions: typing.Optional[typing.List[ManagedSsoClientTaskResultActionsItem]] = pydantic.Field(default=None)
    """
    All actions calculated (desired vs. current), including any that failed to apply.
    """

    applied_actions: typing.Optional[typing.List[ManagedSsoClientTaskResultAppliedActionsItem]] = pydantic.Field(
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
