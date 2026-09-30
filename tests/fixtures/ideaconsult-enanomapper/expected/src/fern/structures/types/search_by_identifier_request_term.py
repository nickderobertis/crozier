

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchByIdentifierRequestTerm(enum.StrEnum):
    SEARCH = "search"
    URL = "url"
    INCHIKEY = "inchikey"

    def visit(
        self,
        search: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
        inchikey: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchByIdentifierRequestTerm.SEARCH:
            return search()
        if self is SearchByIdentifierRequestTerm.URL:
            return url()
        if self is SearchByIdentifierRequestTerm.INCHIKEY:
            return inchikey()
