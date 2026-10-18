

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AssistantSearchRequestSortOrder(enum.StrEnum):
    """
    The order to sort by.
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssistantSearchRequestSortOrder.ASC:
            return asc()
        if self is AssistantSearchRequestSortOrder.DESC:
            return desc()
