

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParseBatchRequestOutputFormat(enum.StrEnum):
    OPENPARSER1 = "openparser@1"
    RAW = "raw"

    def visit(self, openparser1: typing.Callable[[], T_Result], raw: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParseBatchRequestOutputFormat.OPENPARSER1:
            return openparser1()
        if self is ParseBatchRequestOutputFormat.RAW:
            return raw()
