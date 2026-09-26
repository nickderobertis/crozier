

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocManifest200ResponsePagesItemStateRevisionPageKind(enum.StrEnum):
    OBJECT_NUMBER = "objectNumber"

    def visit(self, object_number: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocManifest200ResponsePagesItemStateRevisionPageKind.OBJECT_NUMBER:
            return object_number()
