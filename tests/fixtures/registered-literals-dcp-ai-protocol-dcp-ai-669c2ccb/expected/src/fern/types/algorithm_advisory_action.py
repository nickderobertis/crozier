

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlgorithmAdvisoryAction(enum.StrEnum):
    DEPRECATE = "deprecate"
    WARN = "warn"
    REVOKE = "revoke"

    def visit(
        self,
        deprecate: typing.Callable[[], T_Result],
        warn: typing.Callable[[], T_Result],
        revoke: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AlgorithmAdvisoryAction.DEPRECATE:
            return deprecate()
        if self is AlgorithmAdvisoryAction.WARN:
            return warn()
        if self is AlgorithmAdvisoryAction.REVOKE:
            return revoke()
