

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CockroachSubscribeOpSpecColumnsZero(enum.StrEnum):
    ALL = "*"

    def visit(self, all_: typing.Callable[[], T_Result]) -> T_Result:
        if self is CockroachSubscribeOpSpecColumnsZero.ALL:
            return all_()
