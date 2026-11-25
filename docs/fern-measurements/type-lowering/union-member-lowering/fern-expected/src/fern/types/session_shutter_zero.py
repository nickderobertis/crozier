

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionShutterZero(enum.StrEnum):
    LEAF = "leaf"

    def visit(self, leaf: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionShutterZero.LEAF:
            return leaf()
