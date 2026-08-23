

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateDppRequestRepresentation(enum.StrEnum):
    COMPRESSED = "compressed"
    FULL = "full"

    def visit(self, compressed: typing.Callable[[], T_Result], full: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateDppRequestRepresentation.COMPRESSED:
            return compressed()
        if self is CreateDppRequestRepresentation.FULL:
            return full()
