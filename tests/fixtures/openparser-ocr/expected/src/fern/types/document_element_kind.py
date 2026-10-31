

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentElementKind(enum.StrEnum):
    TEXT = "text"
    TABLE = "table"
    FIGURE = "figure"
    FORMULA = "formula"
    KEY_VALUE = "key_value"
    QUERY_ANSWER = "query_answer"
    SECTION = "section"
    SELECTION_MARK = "selection_mark"
    SIGNATURE = "signature"
    BARCODE = "barcode"
    LINK = "link"
    STAMP = "stamp"
    OTHER = "other"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        table: typing.Callable[[], T_Result],
        figure: typing.Callable[[], T_Result],
        formula: typing.Callable[[], T_Result],
        key_value: typing.Callable[[], T_Result],
        query_answer: typing.Callable[[], T_Result],
        section: typing.Callable[[], T_Result],
        selection_mark: typing.Callable[[], T_Result],
        signature: typing.Callable[[], T_Result],
        barcode: typing.Callable[[], T_Result],
        link: typing.Callable[[], T_Result],
        stamp: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocumentElementKind.TEXT:
            return text()
        if self is DocumentElementKind.TABLE:
            return table()
        if self is DocumentElementKind.FIGURE:
            return figure()
        if self is DocumentElementKind.FORMULA:
            return formula()
        if self is DocumentElementKind.KEY_VALUE:
            return key_value()
        if self is DocumentElementKind.QUERY_ANSWER:
            return query_answer()
        if self is DocumentElementKind.SECTION:
            return section()
        if self is DocumentElementKind.SELECTION_MARK:
            return selection_mark()
        if self is DocumentElementKind.SIGNATURE:
            return signature()
        if self is DocumentElementKind.BARCODE:
            return barcode()
        if self is DocumentElementKind.LINK:
            return link()
        if self is DocumentElementKind.STAMP:
            return stamp()
        if self is DocumentElementKind.OTHER:
            return other()
