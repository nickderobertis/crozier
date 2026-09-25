

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchActionRunIdStatus(enum.StrEnum):
    FAILED = "failed"
    SUCCEEDED = "succeeded"

    def visit(self, failed: typing.Callable[[], T_Result], succeeded: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchActionRunIdStatus.FAILED:
            return failed()
        if self is PatchActionRunIdStatus.SUCCEEDED:
            return succeeded()
