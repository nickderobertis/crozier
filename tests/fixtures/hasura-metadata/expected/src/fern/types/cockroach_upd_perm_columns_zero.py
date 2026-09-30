

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CockroachUpdPermColumnsZero(enum.StrEnum):
    ALL = "*"

    def visit(self, all_: typing.Callable[[], T_Result]) -> T_Result:
        if self is CockroachUpdPermColumnsZero.ALL:
            return all_()
