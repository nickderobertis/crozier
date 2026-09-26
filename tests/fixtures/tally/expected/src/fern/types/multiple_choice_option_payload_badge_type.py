

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MultipleChoiceOptionPayloadBadgeType(enum.StrEnum):
    """
    Badge display type. Only needs to be set on the first option in the group.
    """

    OFF = "OFF"
    NUMBERS = "NUMBERS"
    LETTERS = "LETTERS"

    def visit(
        self,
        off: typing.Callable[[], T_Result],
        numbers: typing.Callable[[], T_Result],
        letters: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MultipleChoiceOptionPayloadBadgeType.OFF:
            return off()
        if self is MultipleChoiceOptionPayloadBadgeType.NUMBERS:
            return numbers()
        if self is MultipleChoiceOptionPayloadBadgeType.LETTERS:
            return letters()
