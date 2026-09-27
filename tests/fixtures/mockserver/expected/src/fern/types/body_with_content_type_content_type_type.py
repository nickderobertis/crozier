

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyWithContentTypeContentTypeType(enum.StrEnum):
    FILE = "FILE"

    def visit(self, file: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyWithContentTypeContentTypeType.FILE:
            return file()
