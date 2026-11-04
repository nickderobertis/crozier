

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Sort(enum.StrEnum):
    """
    An enumeration.
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is Sort.ASC:
            return asc()
        if self is Sort.DESC:
            return desc()
