

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResolutionFilter(enum.StrEnum):
    ALL = "all"
    RESOLVED = "resolved"
    UNRESOLVED = "unresolved"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        resolved: typing.Callable[[], T_Result],
        unresolved: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResolutionFilter.ALL:
            return all_()
        if self is ResolutionFilter.RESOLVED:
            return resolved()
        if self is ResolutionFilter.UNRESOLVED:
            return unresolved()
