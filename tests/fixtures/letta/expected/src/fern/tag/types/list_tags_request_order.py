

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListTagsRequestOrder(enum.StrEnum):
    """
    Sort order for tags. 'asc' for alphabetical order, 'desc' for reverse alphabetical order
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListTagsRequestOrder.ASC:
            return asc()
        if self is ListTagsRequestOrder.DESC:
            return desc()
