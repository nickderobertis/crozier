

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemSquarePageKind(enum.StrEnum):
    OBJECT_NUMBER = "objectNumber"

    def visit(self, object_number: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemSquarePageKind.OBJECT_NUMBER:
            return object_number()
