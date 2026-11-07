

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SpanGeometryInputDisplayMode(enum.StrEnum):
    MIRROR = "mirror"
    SPAN = "span"

    def visit(self, mirror: typing.Callable[[], T_Result], span: typing.Callable[[], T_Result]) -> T_Result:
        if self is SpanGeometryInputDisplayMode.MIRROR:
            return mirror()
        if self is SpanGeometryInputDisplayMode.SPAN:
            return span()
