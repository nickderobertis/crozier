

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SpanStatusDisplayMode(enum.StrEnum):
    MIRROR = "mirror"
    SPAN = "span"

    def visit(self, mirror: typing.Callable[[], T_Result], span: typing.Callable[[], T_Result]) -> T_Result:
        if self is SpanStatusDisplayMode.MIRROR:
            return mirror()
        if self is SpanStatusDisplayMode.SPAN:
            return span()
