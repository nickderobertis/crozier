

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MultipleChoiceOptionBlockGroupType(enum.StrEnum):
    MULTIPLE_CHOICE = "MULTIPLE_CHOICE"

    def visit(self, multiple_choice: typing.Callable[[], T_Result]) -> T_Result:
        if self is MultipleChoiceOptionBlockGroupType.MULTIPLE_CHOICE:
            return multiple_choice()
