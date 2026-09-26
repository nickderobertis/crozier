

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretIntent(enum.StrEnum):
    REPLACE = "replace"

    def visit(self, replace: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretIntent.REPLACE:
            return replace()
