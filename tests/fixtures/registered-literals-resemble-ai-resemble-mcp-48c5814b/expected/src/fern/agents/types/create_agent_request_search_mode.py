

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateAgentRequestSearchMode(enum.StrEnum):
    """
    RAG search strategy - speed (faster) or accuracy (more thorough)
    """

    SPEED = "speed"
    ACCURACY = "accuracy"

    def visit(self, speed: typing.Callable[[], T_Result], accuracy: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateAgentRequestSearchMode.SPEED:
            return speed()
        if self is CreateAgentRequestSearchMode.ACCURACY:
            return accuracy()
