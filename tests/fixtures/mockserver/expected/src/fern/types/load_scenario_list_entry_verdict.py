

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadScenarioListEntryVerdict(enum.StrEnum):
    """
    in-run threshold verdict: PASS (all thresholds satisfied) or FAIL (any breached); absent when the scenario has no thresholds or none has been evaluated yet. A terminal FAIL should be mapped by clients to a non-zero CI exit code.
    """

    PASS = "PASS"
    FAIL = "FAIL"

    def visit(self, pass_: typing.Callable[[], T_Result], fail: typing.Callable[[], T_Result]) -> T_Result:
        if self is LoadScenarioListEntryVerdict.PASS:
            return pass_()
        if self is LoadScenarioListEntryVerdict.FAIL:
            return fail()
