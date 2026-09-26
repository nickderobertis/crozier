

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchAgentRunIdStatus(enum.StrEnum):
    ARCHIVED = "archived"

    def visit(self, archived: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchAgentRunIdStatus.ARCHIVED:
            return archived()
