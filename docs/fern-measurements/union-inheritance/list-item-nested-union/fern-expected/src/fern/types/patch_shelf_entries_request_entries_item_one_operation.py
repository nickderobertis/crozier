

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchShelfEntriesRequestEntriesItemOneOperation(enum.StrEnum):
    DELETE = "delete"

    def visit(self, delete: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchShelfEntriesRequestEntriesItemOneOperation.DELETE:
            return delete()
