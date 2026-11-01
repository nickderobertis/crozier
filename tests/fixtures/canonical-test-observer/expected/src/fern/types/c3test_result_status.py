

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class C3TestResultStatus(enum.StrEnum):
    PASS = "pass"
    FAIL = "fail"
    SKIP = "skip"

    def visit(
        self,
        pass_: typing.Callable[[], T_Result],
        fail: typing.Callable[[], T_Result],
        skip: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is C3TestResultStatus.PASS:
            return pass_()
        if self is C3TestResultStatus.FAIL:
            return fail()
        if self is C3TestResultStatus.SKIP:
            return skip()
