

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReasonUnitSymbol(enum.StrEnum):
    """
    The unit symbol is the symbol used to represent a value.
    """

    TONS = "tons"
    METRE = "metre"
    BOOLEAN = "boolean"
    ENUM = "enum"
    UNKNOWN = "unknown"

    def visit(
        self,
        tons: typing.Callable[[], T_Result],
        metre: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        enum: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReasonUnitSymbol.TONS:
            return tons()
        if self is ReasonUnitSymbol.METRE:
            return metre()
        if self is ReasonUnitSymbol.BOOLEAN:
            return boolean()
        if self is ReasonUnitSymbol.ENUM:
            return enum()
        if self is ReasonUnitSymbol.UNKNOWN:
            return unknown()
