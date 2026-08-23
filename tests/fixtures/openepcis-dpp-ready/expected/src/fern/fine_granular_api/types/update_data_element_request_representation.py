

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateDataElementRequestRepresentation(enum.StrEnum):
    COMPRESSED = "compressed"
    FULL = "full"

    def visit(self, compressed: typing.Callable[[], T_Result], full: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateDataElementRequestRepresentation.COMPRESSED:
            return compressed()
        if self is UpdateDataElementRequestRepresentation.FULL:
            return full()
