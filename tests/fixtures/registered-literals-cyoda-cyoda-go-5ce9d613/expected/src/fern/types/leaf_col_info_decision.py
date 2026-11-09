

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LeafColInfoDecision(enum.StrEnum):
    NO_ACCESS = "NO_ACCESS"
    FULL_ACCESS = "FULL_ACCESS"
    PARTIAL_ACCESS = "PARTIAL_ACCESS"
    NOT_FOUND = "NOT_FOUND"

    def visit(
        self,
        no_access: typing.Callable[[], T_Result],
        full_access: typing.Callable[[], T_Result],
        partial_access: typing.Callable[[], T_Result],
        not_found: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LeafColInfoDecision.NO_ACCESS:
            return no_access()
        if self is LeafColInfoDecision.FULL_ACCESS:
            return full_access()
        if self is LeafColInfoDecision.PARTIAL_ACCESS:
            return partial_access()
        if self is LeafColInfoDecision.NOT_FOUND:
            return not_found()
