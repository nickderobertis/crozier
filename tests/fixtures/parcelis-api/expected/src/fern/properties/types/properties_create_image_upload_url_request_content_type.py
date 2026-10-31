

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PropertiesCreateImageUploadUrlRequestContentType(enum.StrEnum):
    IMAGE_JPEG = "image/jpeg"
    IMAGE_PNG = "image/png"
    IMAGE_WEBP = "image/webp"
    IMAGE_GIF = "image/gif"

    def visit(
        self,
        image_jpeg: typing.Callable[[], T_Result],
        image_png: typing.Callable[[], T_Result],
        image_webp: typing.Callable[[], T_Result],
        image_gif: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PropertiesCreateImageUploadUrlRequestContentType.IMAGE_JPEG:
            return image_jpeg()
        if self is PropertiesCreateImageUploadUrlRequestContentType.IMAGE_PNG:
            return image_png()
        if self is PropertiesCreateImageUploadUrlRequestContentType.IMAGE_WEBP:
            return image_webp()
        if self is PropertiesCreateImageUploadUrlRequestContentType.IMAGE_GIF:
            return image_gif()
