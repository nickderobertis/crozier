

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FdxContentTypes(enum.StrEnum):
    """
    Types of document formats. (Suggested values)
    """

    APPLICATION_PDF = "application/pdf"
    IMAGE_GIF = "image/gif"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_TIFF = "image/tiff"
    IMAGE_PNG = "image/png"
    APPLICATION_JSON = "application/json"

    def visit(
        self,
        application_pdf: typing.Callable[[], T_Result],
        image_gif: typing.Callable[[], T_Result],
        image_jpeg: typing.Callable[[], T_Result],
        image_tiff: typing.Callable[[], T_Result],
        image_png: typing.Callable[[], T_Result],
        application_json: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FdxContentTypes.APPLICATION_PDF:
            return application_pdf()
        if self is FdxContentTypes.IMAGE_GIF:
            return image_gif()
        if self is FdxContentTypes.IMAGE_JPEG:
            return image_jpeg()
        if self is FdxContentTypes.IMAGE_TIFF:
            return image_tiff()
        if self is FdxContentTypes.IMAGE_PNG:
            return image_png()
        if self is FdxContentTypes.APPLICATION_JSON:
            return application_json()
