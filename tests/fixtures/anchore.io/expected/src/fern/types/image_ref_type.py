

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ImageRefType(enum.StrEnum):
    TAG = "tag"
    DIGEST = "digest"
    ID = "id"

    def visit(
        self,
        tag: typing.Callable[[], T_Result],
        digest: typing.Callable[[], T_Result],
        id: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ImageRefType.TAG:
            return tag()
        if self is ImageRefType.DIGEST:
            return digest()
        if self is ImageRefType.ID:
            return id()
