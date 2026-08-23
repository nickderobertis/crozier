

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseType(enum.StrEnum):
    RAW = "raw"
    DOCUMENT = "document"

    def visit(self, raw: typing.Callable[[], T_Result], document: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseType.RAW:
            return raw()
        if self is ResponseType.DOCUMENT:
            return document()
