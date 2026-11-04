

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryRewritingZero(enum.StrEnum):
    """
    Query rewriting disabled, returns query results for query as-is, returns no suggestions for corrected or completed query.
    No performance overhead for spelling correction and suggestions.
    """

    SEARCH_ONLY = "SearchOnly"

    def visit(self, search_only: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryRewritingZero.SEARCH_ONLY:
            return search_only()
