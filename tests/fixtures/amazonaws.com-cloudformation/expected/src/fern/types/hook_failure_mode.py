

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class HookFailureMode(str, enum.Enum):
    FAIL = "FAIL"
    WARN = "WARN"

    def visit(self, fail: typing.Callable[[], T_Result], warn: typing.Callable[[], T_Result]) -> T_Result:
        if self is HookFailureMode.FAIL:
            return fail()
        if self is HookFailureMode.WARN:
            return warn()
