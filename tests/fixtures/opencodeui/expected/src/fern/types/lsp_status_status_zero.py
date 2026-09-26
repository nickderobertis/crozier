

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LspStatusStatusZero(enum.StrEnum):
    CONNECTED = "connected"

    def visit(self, connected: typing.Callable[[], T_Result]) -> T_Result:
        if self is LspStatusStatusZero.CONNECTED:
            return connected()
