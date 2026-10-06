

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetPostsOrder(enum.StrEnum):
    """
    An enumeration.
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetPostsOrder.ASC:
            return asc()
        if self is GetPostsOrder.DESC:
            return desc()
