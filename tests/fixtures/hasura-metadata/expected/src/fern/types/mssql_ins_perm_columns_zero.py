

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MssqlInsPermColumnsZero(enum.StrEnum):
    ALL = "*"

    def visit(self, all_: typing.Callable[[], T_Result]) -> T_Result:
        if self is MssqlInsPermColumnsZero.ALL:
            return all_()
