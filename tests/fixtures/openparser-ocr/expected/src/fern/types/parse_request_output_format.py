

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParseRequestOutputFormat(enum.StrEnum):
    OPENPARSER1 = "openparser@1"
    RAW = "raw"

    def visit(self, openparser1: typing.Callable[[], T_Result], raw: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParseRequestOutputFormat.OPENPARSER1:
            return openparser1()
        if self is ParseRequestOutputFormat.RAW:
            return raw()
