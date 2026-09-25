

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsDocumentsItemContentType(enum.StrEnum):
    APPLICATION_PDF = "application/pdf"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_PNG = "image/png"
    IMAGE_TIFF = "image/tiff"
    IMAGE_WEBP = "image/webp"
    MESSAGE_RFC822 = "message/rfc822"

    def visit(
        self,
        application_pdf: typing.Callable[[], T_Result],
        image_jpeg: typing.Callable[[], T_Result],
        image_png: typing.Callable[[], T_Result],
        image_tiff: typing.Callable[[], T_Result],
        image_webp: typing.Callable[[], T_Result],
        message_rfc822: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocumentsDocumentsItemContentType.APPLICATION_PDF:
            return application_pdf()
        if self is DocumentsDocumentsItemContentType.IMAGE_JPEG:
            return image_jpeg()
        if self is DocumentsDocumentsItemContentType.IMAGE_PNG:
            return image_png()
        if self is DocumentsDocumentsItemContentType.IMAGE_TIFF:
            return image_tiff()
        if self is DocumentsDocumentsItemContentType.IMAGE_WEBP:
            return image_webp()
        if self is DocumentsDocumentsItemContentType.MESSAGE_RFC822:
            return message_rfc822()
