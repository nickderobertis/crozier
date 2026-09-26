

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyToIndexRevisionPageKind(enum.StrEnum):
    OBJECT_NUMBER = "objectNumber"

    def visit(self, object_number: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyToIndexRevisionPageKind.OBJECT_NUMBER:
            return object_number()
