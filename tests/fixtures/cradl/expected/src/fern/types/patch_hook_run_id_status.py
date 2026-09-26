

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchHookRunIdStatus(enum.StrEnum):
    FAILED = "failed"
    IGNORED = "ignored"
    SUCCEEDED = "succeeded"

    def visit(
        self,
        failed: typing.Callable[[], T_Result],
        ignored: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchHookRunIdStatus.FAILED:
            return failed()
        if self is PatchHookRunIdStatus.IGNORED:
            return ignored()
        if self is PatchHookRunIdStatus.SUCCEEDED:
            return succeeded()
