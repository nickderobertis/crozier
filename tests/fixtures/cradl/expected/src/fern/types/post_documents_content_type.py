

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDocumentsContentType(enum.StrEnum):
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
        if self is PostDocumentsContentType.APPLICATION_PDF:
            return application_pdf()
        if self is PostDocumentsContentType.IMAGE_JPEG:
            return image_jpeg()
        if self is PostDocumentsContentType.IMAGE_PNG:
            return image_png()
        if self is PostDocumentsContentType.IMAGE_TIFF:
            return image_tiff()
        if self is PostDocumentsContentType.IMAGE_WEBP:
            return image_webp()
        if self is PostDocumentsContentType.MESSAGE_RFC822:
            return message_rfc822()
