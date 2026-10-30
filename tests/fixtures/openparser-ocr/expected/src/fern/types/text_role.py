

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TextRole(enum.StrEnum):
    DOCUMENT_TITLE = "document_title"
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    LINE = "line"
    WORD = "word"
    SYMBOL = "symbol"
    LIST = "list"
    LIST_ITEM = "list_item"
    CAPTION = "caption"
    FOOTNOTE = "footnote"
    PAGE_HEADER = "page_header"
    PAGE_FOOTER = "page_footer"
    PAGE_NUMBER = "page_number"
    CODE = "code"
    OTHER = "other"

    def visit(
        self,
        document_title: typing.Callable[[], T_Result],
        heading: typing.Callable[[], T_Result],
        paragraph: typing.Callable[[], T_Result],
        line: typing.Callable[[], T_Result],
        word: typing.Callable[[], T_Result],
        symbol: typing.Callable[[], T_Result],
        list_: typing.Callable[[], T_Result],
        list_item: typing.Callable[[], T_Result],
        caption: typing.Callable[[], T_Result],
        footnote: typing.Callable[[], T_Result],
        page_header: typing.Callable[[], T_Result],
        page_footer: typing.Callable[[], T_Result],
        page_number: typing.Callable[[], T_Result],
        code: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TextRole.DOCUMENT_TITLE:
            return document_title()
        if self is TextRole.HEADING:
            return heading()
        if self is TextRole.PARAGRAPH:
            return paragraph()
        if self is TextRole.LINE:
            return line()
        if self is TextRole.WORD:
            return word()
        if self is TextRole.SYMBOL:
            return symbol()
        if self is TextRole.LIST:
            return list_()
        if self is TextRole.LIST_ITEM:
            return list_item()
        if self is TextRole.CAPTION:
            return caption()
        if self is TextRole.FOOTNOTE:
            return footnote()
        if self is TextRole.PAGE_HEADER:
            return page_header()
        if self is TextRole.PAGE_FOOTER:
            return page_footer()
        if self is TextRole.PAGE_NUMBER:
            return page_number()
        if self is TextRole.CODE:
            return code()
        if self is TextRole.OTHER:
            return other()
