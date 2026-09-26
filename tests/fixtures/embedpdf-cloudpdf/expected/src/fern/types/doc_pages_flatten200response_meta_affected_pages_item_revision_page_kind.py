

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocPagesFlatten200ResponseMetaAffectedPagesItemRevisionPageKind(enum.StrEnum):
    OBJECT_NUMBER = "objectNumber"

    def visit(self, object_number: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocPagesFlatten200ResponseMetaAffectedPagesItemRevisionPageKind.OBJECT_NUMBER:
            return object_number()
