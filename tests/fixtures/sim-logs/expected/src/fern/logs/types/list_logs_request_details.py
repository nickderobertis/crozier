

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListLogsRequestDetails(enum.StrEnum):
    """
    Response detail level. `full` adds the `workflow` summary to every workflow run; a job run never carries one, whatever this is set to. `includeTraceSpans=true` and `includeFinalOutput=true` each imply `full`, so either one adds `workflow` even when `details=basic` is sent explicitly.
    """

    BASIC = "basic"
    FULL = "full"

    def visit(self, basic: typing.Callable[[], T_Result], full: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListLogsRequestDetails.BASIC:
            return basic()
        if self is ListLogsRequestDetails.FULL:
            return full()
