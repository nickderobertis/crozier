

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarkerKind(enum.StrEnum):
    MARKER = "Marker"

    def visit(self, marker: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarkerKind.MARKER:
            return marker()
