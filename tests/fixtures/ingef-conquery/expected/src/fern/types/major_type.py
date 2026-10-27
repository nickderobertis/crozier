

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MajorType(enum.StrEnum):
    STRING = "STRING"
    INTEGER = "INTEGER"
    BOOLEAN = "BOOLEAN"
    NUMERIC = "NUMERIC"
    MONEY = "MONEY"
    DATE = "DATE"
    DATE_RANGE = "DATE_RANGE"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        integer: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        numeric: typing.Callable[[], T_Result],
        money: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        date_range: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MajorType.STRING:
            return string()
        if self is MajorType.INTEGER:
            return integer()
        if self is MajorType.BOOLEAN:
            return boolean()
        if self is MajorType.NUMERIC:
            return numeric()
        if self is MajorType.MONEY:
            return money()
        if self is MajorType.DATE:
            return date()
        if self is MajorType.DATE_RANGE:
            return date_range()
