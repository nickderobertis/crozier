

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantDeclarationType(enum.StrEnum):
    PARTICIPANT_DECLARATION = "participant-declaration"

    def visit(self, participant_declaration: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParticipantDeclarationType.PARTICIPANT_DECLARATION:
            return participant_declaration()
