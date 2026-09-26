

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AllowedFilesImageItem(enum.StrEnum):
    ALL = "*"
    JPG = ".jpg"
    JPEG = ".jpeg"
    PNG = ".png"
    GIF = ".gif"
    SVG = ".svg"
    HEIC = ".heic"
    WEBP = ".webp"
    BMP = ".bmp"
    PSD = ".psd"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        jpg: typing.Callable[[], T_Result],
        jpeg: typing.Callable[[], T_Result],
        png: typing.Callable[[], T_Result],
        gif: typing.Callable[[], T_Result],
        svg: typing.Callable[[], T_Result],
        heic: typing.Callable[[], T_Result],
        webp: typing.Callable[[], T_Result],
        bmp: typing.Callable[[], T_Result],
        psd: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AllowedFilesImageItem.ALL:
            return all_()
        if self is AllowedFilesImageItem.JPG:
            return jpg()
        if self is AllowedFilesImageItem.JPEG:
            return jpeg()
        if self is AllowedFilesImageItem.PNG:
            return png()
        if self is AllowedFilesImageItem.GIF:
            return gif()
        if self is AllowedFilesImageItem.SVG:
            return svg()
        if self is AllowedFilesImageItem.HEIC:
            return heic()
        if self is AllowedFilesImageItem.WEBP:
            return webp()
        if self is AllowedFilesImageItem.BMP:
            return bmp()
        if self is AllowedFilesImageItem.PSD:
            return psd()
