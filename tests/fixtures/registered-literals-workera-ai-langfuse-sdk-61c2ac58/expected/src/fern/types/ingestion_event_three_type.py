

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IngestionEventThreeType(enum.StrEnum):
    SPAN_UPDATE = "span-update"

    def visit(self, span_update: typing.Callable[[], T_Result]) -> T_Result:
        if self is IngestionEventThreeType.SPAN_UPDATE:
            return span_update()
