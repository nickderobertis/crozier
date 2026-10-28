

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransectKind(enum.StrEnum):
    TRANSECT = "Transect"

    def visit(self, transect: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransectKind.TRANSECT:
            return transect()
