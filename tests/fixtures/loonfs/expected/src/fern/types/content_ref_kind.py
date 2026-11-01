

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContentRefKind(enum.StrEnum):
    """
    A supported kind of content reference, serialized as a string.
    """

    BLOB_V1 = "blob_v1"

    def visit(self, blob_v1: typing.Callable[[], T_Result]) -> T_Result:
        if self is ContentRefKind.BLOB_V1:
            return blob_v1()
