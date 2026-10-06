

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IdentifierUse(enum.StrEnum):
    USUAL = "USUAL"
    OFFICIAL = "OFFICIAL"
    TEMP = "TEMP"
    SECONDARY = "SECONDARY"
    OLD = "OLD"
    NULL = "NULL"

    def visit(
        self,
        usual: typing.Callable[[], T_Result],
        official: typing.Callable[[], T_Result],
        temp: typing.Callable[[], T_Result],
        secondary: typing.Callable[[], T_Result],
        old: typing.Callable[[], T_Result],
        null: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IdentifierUse.USUAL:
            return usual()
        if self is IdentifierUse.OFFICIAL:
            return official()
        if self is IdentifierUse.TEMP:
            return temp()
        if self is IdentifierUse.SECONDARY:
            return secondary()
        if self is IdentifierUse.OLD:
            return old()
        if self is IdentifierUse.NULL:
            return null()
