

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RawParseResultOutputFormat(enum.StrEnum):
    RAW = "raw"

    def visit(self, raw: typing.Callable[[], T_Result]) -> T_Result:
        if self is RawParseResultOutputFormat.RAW:
            return raw()
