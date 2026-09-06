

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EvalStatusPageConfigSortOrder(enum.StrEnum):
    """
    Sort order (ascending or descending)
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is EvalStatusPageConfigSortOrder.ASC:
            return asc()
        if self is EvalStatusPageConfigSortOrder.DESC:
            return desc()
