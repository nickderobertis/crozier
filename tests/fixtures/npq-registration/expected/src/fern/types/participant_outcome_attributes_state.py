

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantOutcomeAttributesState(enum.StrEnum):
    """
    The state of the outcome (passed or failed)
    """

    PASSED = "passed"
    FAILED = "failed"
    VOIDED = "voided"

    def visit(
        self,
        passed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        voided: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ParticipantOutcomeAttributesState.PASSED:
            return passed()
        if self is ParticipantOutcomeAttributesState.FAILED:
            return failed()
        if self is ParticipantOutcomeAttributesState.VOIDED:
            return voided()
