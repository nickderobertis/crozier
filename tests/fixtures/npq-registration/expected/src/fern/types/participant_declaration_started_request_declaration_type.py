

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantDeclarationStartedRequestDeclarationType(enum.StrEnum):
    """
    The event declaration type
    """

    STARTED = "started"

    def visit(self, started: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParticipantDeclarationStartedRequestDeclarationType.STARTED:
            return started()
