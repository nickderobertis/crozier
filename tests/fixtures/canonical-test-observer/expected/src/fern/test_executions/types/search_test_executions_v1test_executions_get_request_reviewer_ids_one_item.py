

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsOneItem(enum.StrEnum):
    ANY = "any"

    def visit(self, any: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsOneItem.ANY:
            return any()
