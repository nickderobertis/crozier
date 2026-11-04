

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateAgentRequestTurnMode(enum.StrEnum):
    SILENCE = "silence"

    def visit(self, silence: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateAgentRequestTurnMode.SILENCE:
            return silence()
