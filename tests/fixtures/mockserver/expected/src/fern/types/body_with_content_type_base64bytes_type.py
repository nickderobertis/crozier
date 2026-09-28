

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyWithContentTypeBase64BytesType(enum.StrEnum):
    BINARY = "BINARY"

    def visit(self, binary: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyWithContentTypeBase64BytesType.BINARY:
            return binary()
