

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantOutcomeType(enum.StrEnum):
    """
    The data type
    """

    PARTICIPANT_OUTCOME = "participant-outcome"

    def visit(self, participant_outcome: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParticipantOutcomeType.PARTICIPANT_OUTCOME:
            return participant_outcome()
