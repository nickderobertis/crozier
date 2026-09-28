

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodySevenType(enum.StrEnum):
    STRING = "STRING"

    def visit(self, string: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodySevenType.STRING:
            return string()
