

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchModeZero(enum.StrEnum):
    """
    Lexical search mode: Search results are retrieved based on exact matches of query terms with the indexed terms.
    """

    LEXICAL = "Lexical"

    def visit(self, lexical: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchModeZero.LEXICAL:
            return lexical()
