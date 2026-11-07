

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateAgentRequestSearchMode(enum.StrEnum):
    """
    RAG search strategy
    """

    SPEED = "speed"
    ACCURACY = "accuracy"

    def visit(self, speed: typing.Callable[[], T_Result], accuracy: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateAgentRequestSearchMode.SPEED:
            return speed()
        if self is UpdateAgentRequestSearchMode.ACCURACY:
            return accuracy()
