

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SyncKeychainZero(enum.StrEnum):
    COLORED = "Colored"

    def visit(self, colored: typing.Callable[[], T_Result]) -> T_Result:
        if self is SyncKeychainZero.COLORED:
            return colored()
