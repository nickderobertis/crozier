

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SnapStage(enum.StrEnum):
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
        if self is SnapStage.EDGE:
            return edge()
        if self is SnapStage.BETA:
            return beta()
        if self is SnapStage.CANDIDATE:
            return candidate()
        if self is SnapStage.STABLE:
            return stable()
