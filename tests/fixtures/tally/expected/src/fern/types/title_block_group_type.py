

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TitleBlockGroupType(enum.StrEnum):
    TITLE = "TITLE"
    QUESTION = "QUESTION"

    def visit(self, title: typing.Callable[[], T_Result], question: typing.Callable[[], T_Result]) -> T_Result:
        if self is TitleBlockGroupType.TITLE:
            return title()
        if self is TitleBlockGroupType.QUESTION:
            return question()
