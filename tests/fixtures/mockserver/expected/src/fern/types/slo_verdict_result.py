

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SloVerdictResult(enum.StrEnum):
    PASS = "PASS"
    FAIL = "FAIL"
    INCONCLUSIVE = "INCONCLUSIVE"

    def visit(
        self,
        pass_: typing.Callable[[], T_Result],
        fail: typing.Callable[[], T_Result],
        inconclusive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SloVerdictResult.PASS:
            return pass_()
        if self is SloVerdictResult.FAIL:
            return fail()
        if self is SloVerdictResult.INCONCLUSIVE:
            return inconclusive()
