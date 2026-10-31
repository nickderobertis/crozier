

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FieldDatatype(enum.StrEnum):
    """
    The data type of the field in question (text, numeric, date, select_single, select_multiple or labels). The labels type belongs to the Labels field, which comes into being by itself as soon as your list has at least one label; you do not create that field yourself.
    """

    TEXT = "text"
    NUMERIC = "numeric"
    DATE = "date"
    SELECT_SINGLE = "select_single"
    SELECT_MULTIPLE = "select_multiple"
    LABELS = "labels"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        numeric: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        select_single: typing.Callable[[], T_Result],
        select_multiple: typing.Callable[[], T_Result],
        labels: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FieldDatatype.TEXT:
            return text()
        if self is FieldDatatype.NUMERIC:
            return numeric()
        if self is FieldDatatype.DATE:
            return date()
        if self is FieldDatatype.SELECT_SINGLE:
            return select_single()
        if self is FieldDatatype.SELECT_MULTIPLE:
            return select_multiple()
        if self is FieldDatatype.LABELS:
            return labels()
