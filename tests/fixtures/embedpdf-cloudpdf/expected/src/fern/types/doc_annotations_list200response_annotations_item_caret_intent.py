

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemCaretIntent(enum.StrEnum):
    REPLACE = "replace"

    def visit(self, replace: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemCaretIntent.REPLACE:
            return replace()
