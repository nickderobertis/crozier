

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LookupTableNotePartType(enum.StrEnum):
    LOOKUP_TABLE = "lookup_table"

    def visit(self, lookup_table: typing.Callable[[], T_Result]) -> T_Result:
        if self is LookupTableNotePartType.LOOKUP_TABLE:
            return lookup_table()
