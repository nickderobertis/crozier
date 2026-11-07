

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PrepareUploadMetaRequestContentType(enum.StrEnum):
    IMAGE_PNG = "image/png"
    IMAGE_JPEG = "image/jpeg"
    APPLICATION_PDF = "application/pdf"

    def visit(
        self,
        image_png: typing.Callable[[], T_Result],
        image_jpeg: typing.Callable[[], T_Result],
        application_pdf: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PrepareUploadMetaRequestContentType.IMAGE_PNG:
            return image_png()
        if self is PrepareUploadMetaRequestContentType.IMAGE_JPEG:
            return image_jpeg()
        if self is PrepareUploadMetaRequestContentType.APPLICATION_PDF:
            return application_pdf()
