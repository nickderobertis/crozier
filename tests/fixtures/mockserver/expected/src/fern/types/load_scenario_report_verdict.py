

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadScenarioReportVerdict(enum.StrEnum):
    """
    in-run threshold verdict; absent when the scenario has no thresholds or none has been evaluated yet
    """

    PASS = "PASS"
    FAIL = "FAIL"

    def visit(self, pass_: typing.Callable[[], T_Result], fail: typing.Callable[[], T_Result]) -> T_Result:
        if self is LoadScenarioReportVerdict.PASS:
            return pass_()
        if self is LoadScenarioReportVerdict.FAIL:
            return fail()
