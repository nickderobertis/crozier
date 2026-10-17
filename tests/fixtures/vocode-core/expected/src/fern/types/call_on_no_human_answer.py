

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CallOnNoHumanAnswer(enum.StrEnum):
    CONTINUE = "continue"
    HANGUP = "hangup"

    def visit(self, continue_: typing.Callable[[], T_Result], hangup: typing.Callable[[], T_Result]) -> T_Result:
        if self is CallOnNoHumanAnswer.CONTINUE:
            return continue_()
        if self is CallOnNoHumanAnswer.HANGUP:
            return hangup()
