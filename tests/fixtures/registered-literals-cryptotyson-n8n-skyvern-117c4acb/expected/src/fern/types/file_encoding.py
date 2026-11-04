

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileEncoding(enum.StrEnum):
    """
    Supported file content encodings.
    """

    BASE64 = "base64"

    def visit(self, base64: typing.Callable[[], T_Result]) -> T_Result:
        if self is FileEncoding.BASE64:
            return base64()
