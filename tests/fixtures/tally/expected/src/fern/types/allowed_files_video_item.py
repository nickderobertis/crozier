

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AllowedFilesVideoItem(enum.StrEnum):
    ALL = "*"
    MP4 = ".mp4"
    MOV = ".mov"
    WEBM = ".webm"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        mp4: typing.Callable[[], T_Result],
        mov: typing.Callable[[], T_Result],
        webm: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AllowedFilesVideoItem.ALL:
            return all_()
        if self is AllowedFilesVideoItem.MP4:
            return mp4()
        if self is AllowedFilesVideoItem.MOV:
            return mov()
        if self is AllowedFilesVideoItem.WEBM:
            return webm()
