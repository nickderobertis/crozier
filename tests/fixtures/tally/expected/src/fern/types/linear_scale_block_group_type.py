

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinearScaleBlockGroupType(enum.StrEnum):
    QUESTION = "QUESTION"

    def visit(self, question: typing.Callable[[], T_Result]) -> T_Result:
        if self is LinearScaleBlockGroupType.QUESTION:
            return question()
