

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataconnectorInsPermColumnsZero(enum.StrEnum):
    ALL = "*"

    def visit(self, all_: typing.Callable[[], T_Result]) -> T_Result:
        if self is DataconnectorInsPermColumnsZero.ALL:
            return all_()
