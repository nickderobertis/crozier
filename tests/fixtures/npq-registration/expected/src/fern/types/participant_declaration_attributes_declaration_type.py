

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantDeclarationAttributesDeclarationType(enum.StrEnum):
    """
    The event declaration type
    """

    STARTED = "started"
    RETAINED1 = "retained-1"
    RETAINED2 = "retained-2"
    COMPLETED = "completed"

    def visit(
        self,
        started: typing.Callable[[], T_Result],
        retained1: typing.Callable[[], T_Result],
        retained2: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ParticipantDeclarationAttributesDeclarationType.STARTED:
            return started()
        if self is ParticipantDeclarationAttributesDeclarationType.RETAINED1:
            return retained1()
        if self is ParticipantDeclarationAttributesDeclarationType.RETAINED2:
            return retained2()
        if self is ParticipantDeclarationAttributesDeclarationType.COMPLETED:
            return completed()
