

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FilterLang(enum.StrEnum):
    """
    Filter encoding used in the filter parameter
    """

    CQL_TEXT = "cql-text"
    CQL2TEXT = "cql2-text"

    def visit(self, cql_text: typing.Callable[[], T_Result], cql2text: typing.Callable[[], T_Result]) -> T_Result:
        if self is FilterLang.CQL_TEXT:
            return cql_text()
        if self is FilterLang.CQL2TEXT:
            return cql2text()
