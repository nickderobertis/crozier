

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TermsAndConditionsItemType(enum.StrEnum):
    """
    Role for which this TnC applies
    """

    PARTICIPANT = "Participant"
    DIRECTORY = "Directory"

    def visit(self, participant: typing.Callable[[], T_Result], directory: typing.Callable[[], T_Result]) -> T_Result:
        if self is TermsAndConditionsItemType.PARTICIPANT:
            return participant()
        if self is TermsAndConditionsItemType.DIRECTORY:
            return directory()
