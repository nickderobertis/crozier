

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MultipleChoiceBlockGroupType(enum.StrEnum):
    QUESTION = "QUESTION"

    def visit(self, question: typing.Callable[[], T_Result]) -> T_Result:
        if self is MultipleChoiceBlockGroupType.QUESTION:
            return question()
