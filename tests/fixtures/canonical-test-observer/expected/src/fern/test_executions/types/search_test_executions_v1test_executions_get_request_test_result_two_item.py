

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchTestExecutionsV1TestExecutionsGetRequestTestResultTwoItem(enum.StrEnum):
    NONE = "none"

    def visit(self, none: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchTestExecutionsV1TestExecutionsGetRequestTestResultTwoItem.NONE:
            return none()
