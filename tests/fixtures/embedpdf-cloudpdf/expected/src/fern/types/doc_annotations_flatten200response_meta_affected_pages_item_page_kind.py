

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsFlatten200ResponseMetaAffectedPagesItemPageKind(enum.StrEnum):
    OBJECT_NUMBER = "objectNumber"

    def visit(self, object_number: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsFlatten200ResponseMetaAffectedPagesItemPageKind.OBJECT_NUMBER:
            return object_number()
