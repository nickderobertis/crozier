

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AfterActionFailurePolicy(enum.StrEnum):
    FAIL_FAST = "FAIL_FAST"
    BEST_EFFORT = "BEST_EFFORT"

    def visit(self, fail_fast: typing.Callable[[], T_Result], best_effort: typing.Callable[[], T_Result]) -> T_Result:
        if self is AfterActionFailurePolicy.FAIL_FAST:
            return fail_fast()
        if self is AfterActionFailurePolicy.BEST_EFFORT:
            return best_effort()
