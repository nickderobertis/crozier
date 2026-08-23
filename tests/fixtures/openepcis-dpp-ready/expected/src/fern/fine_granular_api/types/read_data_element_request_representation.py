

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ReadDataElementRequestRepresentation(enum.StrEnum):
    COMPRESSED = "compressed"
    FULL = "full"

    def visit(self, compressed: typing.Callable[[], T_Result], full: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReadDataElementRequestRepresentation.COMPRESSED:
            return compressed()
        if self is ReadDataElementRequestRepresentation.FULL:
            return full()
