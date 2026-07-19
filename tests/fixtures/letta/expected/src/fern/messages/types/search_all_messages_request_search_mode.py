

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchAllMessagesRequestSearchMode(enum.StrEnum):
    """
    Search mode to use
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
        if self is SearchAllMessagesRequestSearchMode.VECTOR:
            return vector()
        if self is SearchAllMessagesRequestSearchMode.FTS:
            return fts()
        if self is SearchAllMessagesRequestSearchMode.HYBRID:
            return hybrid()
