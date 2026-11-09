

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateEmbeddingRequestEncodingFormat(enum.StrEnum):
    """
    The format to return the embeddings in. Can be either `float` or [`base64`](https://pypi.org/project/pybase64/).
    """

    FLOAT = "float"
    BASE64 = "base64"

    def visit(self, float_: typing.Callable[[], T_Result], base64: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateEmbeddingRequestEncodingFormat.FLOAT:
            return float_()
        if self is CreateEmbeddingRequestEncodingFormat.BASE64:
            return base64()
