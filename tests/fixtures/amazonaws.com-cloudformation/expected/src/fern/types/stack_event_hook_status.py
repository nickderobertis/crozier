

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackEventHookStatus(enum.StrEnum):
    """
    Provides the status of the change set hook.
    """

    HOOK_IN_PROGRESS = "HOOK_IN_PROGRESS"
    HOOK_COMPLETE_SUCCEEDED = "HOOK_COMPLETE_SUCCEEDED"
    HOOK_COMPLETE_FAILED = "HOOK_COMPLETE_FAILED"
    HOOK_FAILED = "HOOK_FAILED"

    def visit(
        self,
        hook_in_progress: typing.Callable[[], T_Result],
        hook_complete_succeeded: typing.Callable[[], T_Result],
        hook_complete_failed: typing.Callable[[], T_Result],
        hook_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackEventHookStatus.HOOK_IN_PROGRESS:
            return hook_in_progress()
        if self is StackEventHookStatus.HOOK_COMPLETE_SUCCEEDED:
            return hook_complete_succeeded()
        if self is StackEventHookStatus.HOOK_COMPLETE_FAILED:
            return hook_complete_failed()
        if self is StackEventHookStatus.HOOK_FAILED:
            return hook_failed()
