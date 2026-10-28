

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchPostRequestFilterLang(enum.StrEnum):
    CQL2JSON = "cql2-json"

    def visit(self, cql2json: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchPostRequestFilterLang.CQL2JSON:
            return cql2json()
