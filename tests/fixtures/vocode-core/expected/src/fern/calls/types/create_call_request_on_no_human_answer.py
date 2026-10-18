

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateCallRequestOnNoHumanAnswer(enum.StrEnum):
    CONTINUE = "continue"
    HANGUP = "hangup"

    def visit(self, continue_: typing.Callable[[], T_Result], hangup: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateCallRequestOnNoHumanAnswer.CONTINUE:
            return continue_()
        if self is CreateCallRequestOnNoHumanAnswer.HANGUP:
            return hangup()
