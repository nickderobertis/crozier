

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantDeclarationRetainedRequestDeclarationType(enum.StrEnum):
    """
    The event declaration type
    """

    RETAINED1 = "retained-1"
    RETAINED2 = "retained-2"

    def visit(self, retained1: typing.Callable[[], T_Result], retained2: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParticipantDeclarationRetainedRequestDeclarationType.RETAINED1:
            return retained1()
        if self is ParticipantDeclarationRetainedRequestDeclarationType.RETAINED2:
            return retained2()
