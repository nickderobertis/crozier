

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class EmbeddingsRequestEncodingFormat(enum.StrEnum):
    FLOAT = "float"
    BASE64 = "base64"

    def visit(self, float_: typing.Callable[[], T_Result], base64: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmbeddingsRequestEncodingFormat.FLOAT:
            return float_()
        if self is EmbeddingsRequestEncodingFormat.BASE64:
            return base64()
