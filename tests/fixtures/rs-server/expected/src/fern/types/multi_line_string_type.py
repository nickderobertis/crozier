

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MultiLineStringType(enum.StrEnum):
    MULTI_LINE_STRING = "MultiLineString"

    def visit(self, multi_line_string: typing.Callable[[], T_Result]) -> T_Result:
        if self is MultiLineStringType.MULTI_LINE_STRING:
            return multi_line_string()
