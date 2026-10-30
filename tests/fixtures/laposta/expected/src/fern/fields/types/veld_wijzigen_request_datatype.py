

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class VeldWijzigenRequestDatatype(enum.StrEnum):
    """
    The data type of this field (text, numeric, date, select_single, select_multiple)
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
        if self is VeldWijzigenRequestDatatype.TEXT:
            return text()
        if self is VeldWijzigenRequestDatatype.NUMERIC:
            return numeric()
        if self is VeldWijzigenRequestDatatype.DATE:
            return date()
        if self is VeldWijzigenRequestDatatype.SELECT_SINGLE:
            return select_single()
        if self is VeldWijzigenRequestDatatype.SELECT_MULTIPLE:
            return select_multiple()
