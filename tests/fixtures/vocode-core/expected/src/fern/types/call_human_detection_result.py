

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CallHumanDetectionResult(enum.StrEnum):
    HUMAN = "human"
    NO_HUMAN = "no_human"

    def visit(self, human: typing.Callable[[], T_Result], no_human: typing.Callable[[], T_Result]) -> T_Result:
        if self is CallHumanDetectionResult.HUMAN:
            return human()
        if self is CallHumanDetectionResult.NO_HUMAN:
            return no_human()
