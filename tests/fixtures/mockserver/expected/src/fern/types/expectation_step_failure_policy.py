

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExpectationStepFailurePolicy(enum.StrEnum):
    FAIL_FAST = "FAIL_FAST"
    BEST_EFFORT = "BEST_EFFORT"

    def visit(self, fail_fast: typing.Callable[[], T_Result], best_effort: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExpectationStepFailurePolicy.FAIL_FAST:
            return fail_fast()
        if self is ExpectationStepFailurePolicy.BEST_EFFORT:
            return best_effort()
