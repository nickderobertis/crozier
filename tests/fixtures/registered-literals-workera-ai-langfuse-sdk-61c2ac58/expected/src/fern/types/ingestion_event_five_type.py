

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IngestionEventFiveType(enum.StrEnum):
    GENERATION_UPDATE = "generation-update"

    def visit(self, generation_update: typing.Callable[[], T_Result]) -> T_Result:
        if self is IngestionEventFiveType.GENERATION_UPDATE:
            return generation_update()
