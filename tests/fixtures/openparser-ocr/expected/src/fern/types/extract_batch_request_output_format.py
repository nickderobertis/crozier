

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractBatchRequestOutputFormat(enum.StrEnum):
    OPENPARSER1 = "openparser@1"
    RAW = "raw"

    def visit(self, openparser1: typing.Callable[[], T_Result], raw: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExtractBatchRequestOutputFormat.OPENPARSER1:
            return openparser1()
        if self is ExtractBatchRequestOutputFormat.RAW:
            return raw()
