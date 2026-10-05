

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .quay_repos_task_result_actions_item import QuayReposTaskResultActionsItem
from .quay_repos_task_result_applied_actions_item import QuayReposTaskResultAppliedActionsItem
from .task_status import TaskStatus


class QuayReposTaskResult(UniversalBaseModel):
    """
    Result of a completed reconciliation task.
    """

    actions: typing.Optional[typing.List[QuayReposTaskResultActionsItem]] = pydantic.Field(default=None)
    """
    All actions calculated (desired - current).
    """

    applied_actions: typing.Optional[typing.List[QuayReposTaskResultAppliedActionsItem]] = pydantic.Field(default=None)
    """
    Actions successfully applied (non-dry-run only).
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
