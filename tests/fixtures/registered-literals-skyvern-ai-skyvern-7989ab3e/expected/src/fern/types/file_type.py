

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileType(enum.StrEnum):
    AUTO_DETECT = "auto_detect"
    CSV = "csv"
    EXCEL = "excel"
    PDF = "pdf"
    IMAGE = "image"
    DOCX = "docx"
    ZIP = "zip"

    def visit(
        self,
        auto_detect: typing.Callable[[], T_Result],
        csv: typing.Callable[[], T_Result],
        excel: typing.Callable[[], T_Result],
        pdf: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
        docx: typing.Callable[[], T_Result],
        zip: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FileType.AUTO_DETECT:
            return auto_detect()
        if self is FileType.CSV:
            return csv()
        if self is FileType.EXCEL:
            return excel()
        if self is FileType.PDF:
            return pdf()
        if self is FileType.IMAGE:
            return image()
        if self is FileType.DOCX:
            return docx()
        if self is FileType.ZIP:
            return zip()
