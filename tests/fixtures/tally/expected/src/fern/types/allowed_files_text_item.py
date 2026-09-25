

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AllowedFilesTextItem(enum.StrEnum):
    ALL = "*"
    TXT = ".txt"
    CSV = ".csv"
    HTML = ".html"
    XML = ".xml"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        txt: typing.Callable[[], T_Result],
        csv: typing.Callable[[], T_Result],
        html: typing.Callable[[], T_Result],
        xml: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AllowedFilesTextItem.ALL:
            return all_()
        if self is AllowedFilesTextItem.TXT:
            return txt()
        if self is AllowedFilesTextItem.CSV:
            return csv()
        if self is AllowedFilesTextItem.HTML:
            return html()
        if self is AllowedFilesTextItem.XML:
            return xml()
