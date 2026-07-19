

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ToolSearchRequestSearchMode(enum.StrEnum):
    """
    Search mode: vector, fts, or hybrid.
    """

    VECTOR = "vector"
    FTS = "fts"
    HYBRID = "hybrid"

    def visit(
        self,
        vector: typing.Callable[[], T_Result],
        fts: typing.Callable[[], T_Result],
        hybrid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ToolSearchRequestSearchMode.VECTOR:
            return vector()
        if self is ToolSearchRequestSearchMode.FTS:
            return fts()
        if self is ToolSearchRequestSearchMode.HYBRID:
            return hybrid()
