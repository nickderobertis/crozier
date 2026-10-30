

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class VeldToevoegenRequestDatatype(enum.StrEnum):
    """
    The data type: text, numeric, date, select_single or select_multiple
    """

    TEXT = "text"
    NUMERIC = "numeric"
    DATE = "date"
    SELECT_SINGLE = "select_single"
    SELECT_MULTIPLE = "select_multiple"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        numeric: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        select_single: typing.Callable[[], T_Result],
        select_multiple: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VeldToevoegenRequestDatatype.TEXT:
            return text()
        if self is VeldToevoegenRequestDatatype.NUMERIC:
            return numeric()
        if self is VeldToevoegenRequestDatatype.DATE:
            return date()
        if self is VeldToevoegenRequestDatatype.SELECT_SINGLE:
            return select_single()
        if self is VeldToevoegenRequestDatatype.SELECT_MULTIPLE:
            return select_multiple()
