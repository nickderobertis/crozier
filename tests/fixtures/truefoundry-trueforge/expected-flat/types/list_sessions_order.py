

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListSessionsOrder(enum.StrEnum):
    """
    Sort sessions by `updated_at`. Defaults to "desc".
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListSessionsOrder.ASC:
            return asc()
        if self is ListSessionsOrder.DESC:
            return desc()
