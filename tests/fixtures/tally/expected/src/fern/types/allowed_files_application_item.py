

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AllowedFilesApplicationItem(enum.StrEnum):
    ALL = "*"
    PDF = ".pdf"
    DOC = ".doc"
    DOCX = ".docx"
    XLS = ".xls"
    XLSX = ".xlsx"
    PPT = ".ppt"
    PPTX = ".pptx"
    ZIP = ".zip"
    RAR = ".rar"
    JSON = ".json"
    GZIP = ".gzip"
    ODT = ".odt"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        pdf: typing.Callable[[], T_Result],
        doc: typing.Callable[[], T_Result],
        docx: typing.Callable[[], T_Result],
        xls: typing.Callable[[], T_Result],
        xlsx: typing.Callable[[], T_Result],
        ppt: typing.Callable[[], T_Result],
        pptx: typing.Callable[[], T_Result],
        zip: typing.Callable[[], T_Result],
        rar: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
        gzip: typing.Callable[[], T_Result],
        odt: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AllowedFilesApplicationItem.ALL:
            return all_()
        if self is AllowedFilesApplicationItem.PDF:
            return pdf()
        if self is AllowedFilesApplicationItem.DOC:
            return doc()
        if self is AllowedFilesApplicationItem.DOCX:
            return docx()
        if self is AllowedFilesApplicationItem.XLS:
            return xls()
        if self is AllowedFilesApplicationItem.XLSX:
            return xlsx()
        if self is AllowedFilesApplicationItem.PPT:
            return ppt()
        if self is AllowedFilesApplicationItem.PPTX:
            return pptx()
        if self is AllowedFilesApplicationItem.ZIP:
            return zip()
        if self is AllowedFilesApplicationItem.RAR:
            return rar()
        if self is AllowedFilesApplicationItem.JSON:
            return json()
        if self is AllowedFilesApplicationItem.GZIP:
            return gzip()
        if self is AllowedFilesApplicationItem.ODT:
            return odt()
