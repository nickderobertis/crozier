

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem(enum.StrEnum):
    HEIC = "heic"
    PNG = "png"
    JPEG = "jpeg"
    JPG = "jpg"
    WEBP = "webp"
    PDF = "pdf"
    EML = "eml"
    DOC = "doc"
    DOCX = "docx"
    XLS = "xls"
    XLSX = "xlsx"
    PPT = "ppt"
    PPTX = "pptx"
    TXT = "txt"
    CSV = "csv"
    MP4 = "mp4"
    MOV = "mov"
    AVI = "avi"
    MKV = "mkv"
    WEBM = "webm"
    ZIP = "zip"
    RAR = "rar"
    SEVEN_Z = "7z"
    TAR = "tar"

    def visit(
        self,
        heic: typing.Callable[[], T_Result],
        png: typing.Callable[[], T_Result],
        jpeg: typing.Callable[[], T_Result],
        jpg: typing.Callable[[], T_Result],
        webp: typing.Callable[[], T_Result],
        pdf: typing.Callable[[], T_Result],
        eml: typing.Callable[[], T_Result],
        doc: typing.Callable[[], T_Result],
        docx: typing.Callable[[], T_Result],
        xls: typing.Callable[[], T_Result],
        xlsx: typing.Callable[[], T_Result],
        ppt: typing.Callable[[], T_Result],
        pptx: typing.Callable[[], T_Result],
        txt: typing.Callable[[], T_Result],
        csv: typing.Callable[[], T_Result],
        mp4: typing.Callable[[], T_Result],
        mov: typing.Callable[[], T_Result],
        avi: typing.Callable[[], T_Result],
        mkv: typing.Callable[[], T_Result],
        webm: typing.Callable[[], T_Result],
        zip: typing.Callable[[], T_Result],
        rar: typing.Callable[[], T_Result],
        seven_z: typing.Callable[[], T_Result],
        tar: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.HEIC:
            return heic()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.PNG:
            return png()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.JPEG:
            return jpeg()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.JPG:
            return jpg()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.WEBP:
            return webp()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.PDF:
            return pdf()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.EML:
            return eml()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.DOC:
            return doc()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.DOCX:
            return docx()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.XLS:
            return xls()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.XLSX:
            return xlsx()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.PPT:
            return ppt()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.PPTX:
            return pptx()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.TXT:
            return txt()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.CSV:
            return csv()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.MP4:
            return mp4()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.MOV:
            return mov()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.AVI:
            return avi()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.MKV:
            return mkv()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.WEBM:
            return webm()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.ZIP:
            return zip()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.RAR:
            return rar()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.SEVEN_Z:
            return seven_z()
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem.TAR:
            return tar()
