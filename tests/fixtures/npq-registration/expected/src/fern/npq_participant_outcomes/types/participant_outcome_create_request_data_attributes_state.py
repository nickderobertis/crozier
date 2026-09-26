

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantOutcomeCreateRequestDataAttributesState(enum.StrEnum):
    """
    The state of the outcome (passed or failed)
    """

    PASSED = "passed"
    FAILED = "failed"

    def visit(self, passed: typing.Callable[[], T_Result], failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParticipantOutcomeCreateRequestDataAttributesState.PASSED:
            return passed()
        if self is ParticipantOutcomeCreateRequestDataAttributesState.FAILED:
            return failed()
