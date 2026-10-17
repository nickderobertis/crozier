

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NormalizedCallOnNoHumanAnswer(enum.StrEnum):
    CONTINUE = "continue"
    HANGUP = "hangup"

    def visit(self, continue_: typing.Callable[[], T_Result], hangup: typing.Callable[[], T_Result]) -> T_Result:
        if self is NormalizedCallOnNoHumanAnswer.CONTINUE:
            return continue_()
        if self is NormalizedCallOnNoHumanAnswer.HANGUP:
            return hangup()
