

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BuildState(enum.StrEnum):
    MISSING = "missing"
    IN_PROGRESS = "in_progress"
    BUILD_COMPLETED = "build_completed"
    COMPLETED = "completed"
    FAILED = "failed"

    def visit(
        self,
        missing: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        build_completed: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BuildState.MISSING:
            return missing()
        if self is BuildState.IN_PROGRESS:
            return in_progress()
        if self is BuildState.BUILD_COMPLETED:
            return build_completed()
        if self is BuildState.COMPLETED:
            return completed()
        if self is BuildState.FAILED:
            return failed()
