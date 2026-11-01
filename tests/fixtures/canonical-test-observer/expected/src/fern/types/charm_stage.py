

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CharmStage(enum.StrEnum):
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
        if self is CharmStage.EDGE:
            return edge()
        if self is CharmStage.BETA:
            return beta()
        if self is CharmStage.CANDIDATE:
            return candidate()
        if self is CharmStage.STABLE:
            return stable()
