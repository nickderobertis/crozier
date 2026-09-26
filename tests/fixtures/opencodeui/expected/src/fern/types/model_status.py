

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelStatus(enum.StrEnum):
    ALPHA = "alpha"
    BETA = "beta"
    DEPRECATED = "deprecated"
    ACTIVE = "active"

    def visit(
        self,
        alpha: typing.Callable[[], T_Result],
        beta: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ModelStatus.ALPHA:
            return alpha()
        if self is ModelStatus.BETA:
            return beta()
        if self is ModelStatus.DEPRECATED:
            return deprecated()
        if self is ModelStatus.ACTIVE:
            return active()
