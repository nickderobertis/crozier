

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSiblingDiscountsV3RequestSiblingFilter(enum.StrEnum):
    TWINS = "twins"
    MANY_SIBLINGS = "many_siblings"

    def visit(self, twins: typing.Callable[[], T_Result], many_siblings: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetSiblingDiscountsV3RequestSiblingFilter.TWINS:
            return twins()
        if self is GetSiblingDiscountsV3RequestSiblingFilter.MANY_SIBLINGS:
            return many_siblings()
