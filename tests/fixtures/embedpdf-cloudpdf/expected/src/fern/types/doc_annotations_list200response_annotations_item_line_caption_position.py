

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemLineCaptionPosition(enum.StrEnum):
    INLINE = "inline"
    TOP = "top"

    def visit(self, inline: typing.Callable[[], T_Result], top: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemLineCaptionPosition.INLINE:
            return inline()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineCaptionPosition.TOP:
            return top()
