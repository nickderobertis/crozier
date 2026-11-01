

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StageName(enum.StrEnum):
    PROPOSED = "proposed"
    UPDATES = "updates"
    EDGE = "edge"
    BETA = "beta"
    CANDIDATE = "candidate"
    STABLE = "stable"
    PENDING = "pending"
    CURRENT = "current"

    def visit(
        self,
        proposed: typing.Callable[[], T_Result],
        updates: typing.Callable[[], T_Result],
        edge: typing.Callable[[], T_Result],
        beta: typing.Callable[[], T_Result],
        candidate: typing.Callable[[], T_Result],
        stable: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        current: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StageName.PROPOSED:
            return proposed()
        if self is StageName.UPDATES:
            return updates()
        if self is StageName.EDGE:
            return edge()
        if self is StageName.BETA:
            return beta()
        if self is StageName.CANDIDATE:
            return candidate()
        if self is StageName.STABLE:
            return stable()
        if self is StageName.PENDING:
            return pending()
        if self is StageName.CURRENT:
            return current()
