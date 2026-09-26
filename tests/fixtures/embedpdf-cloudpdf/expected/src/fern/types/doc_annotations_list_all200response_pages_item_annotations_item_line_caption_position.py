

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineCaptionPosition(enum.StrEnum):
    INLINE = "inline"
    TOP = "top"

    def visit(self, inline: typing.Callable[[], T_Result], top: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineCaptionPosition.INLINE:
            return inline()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineCaptionPosition.TOP:
            return top()
