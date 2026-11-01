

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchTestExecutionsV1TestExecutionsGetRequestEventNamesOneItem(enum.StrEnum):
    ANY = "any"

    def visit(self, any: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchTestExecutionsV1TestExecutionsGetRequestEventNamesOneItem.ANY:
            return any()
