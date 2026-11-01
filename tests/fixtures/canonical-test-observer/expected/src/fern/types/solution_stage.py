

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SolutionStage(enum.StrEnum):
    EDGE = "edge"
    BETA = "beta"
    CANDIDATE = "candidate"
    STABLE = "stable"

    def visit(
        self,
        edge: typing.Callable[[], T_Result],
        beta: typing.Callable[[], T_Result],
        candidate: typing.Callable[[], T_Result],
        stable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SolutionStage.EDGE:
            return edge()
        if self is SolutionStage.BETA:
            return beta()
        if self is SolutionStage.CANDIDATE:
            return candidate()
        if self is SolutionStage.STABLE:
            return stable()
