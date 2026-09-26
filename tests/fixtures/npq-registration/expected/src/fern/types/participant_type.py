

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantType(enum.StrEnum):
    """
    The data type
    """

    NPQ_PARTICIPANT = "npq-participant"

    def visit(self, npq_participant: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParticipantType.NPQ_PARTICIPANT:
            return npq_participant()
