

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IngestionEventFourType(enum.StrEnum):
    GENERATION_CREATE = "generation-create"

    def visit(self, generation_create: typing.Callable[[], T_Result]) -> T_Result:
        if self is IngestionEventFourType.GENERATION_CREATE:
            return generation_create()
