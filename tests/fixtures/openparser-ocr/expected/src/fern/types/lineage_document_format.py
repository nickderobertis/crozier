

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LineageDocumentFormat(enum.StrEnum):
    LINEAGE1 = "lineage@1"

    def visit(self, lineage1: typing.Callable[[], T_Result]) -> T_Result:
        if self is LineageDocumentFormat.LINEAGE1:
            return lineage1()
