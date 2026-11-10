

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IngestionEventTwoType(enum.StrEnum):
    SPAN_CREATE = "span-create"

    def visit(self, span_create: typing.Callable[[], T_Result]) -> T_Result:
        if self is IngestionEventTwoType.SPAN_CREATE:
            return span_create()
