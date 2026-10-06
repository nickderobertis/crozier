

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchEntryMode(enum.StrEnum):
    MATCH = "MATCH"
    INCLUDE = "INCLUDE"
    OUTCOME = "OUTCOME"
    NULL = "NULL"

    def visit(
        self,
        match: typing.Callable[[], T_Result],
        include: typing.Callable[[], T_Result],
        outcome: typing.Callable[[], T_Result],
        null: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchEntryMode.MATCH:
            return match()
        if self is SearchEntryMode.INCLUDE:
            return include()
        if self is SearchEntryMode.OUTCOME:
            return outcome()
        if self is SearchEntryMode.NULL:
            return null()
