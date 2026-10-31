

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParsedDocumentOutputFormat(enum.StrEnum):
    OPENPARSER1 = "openparser@1"

    def visit(self, openparser1: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParsedDocumentOutputFormat.OPENPARSER1:
            return openparser1()
