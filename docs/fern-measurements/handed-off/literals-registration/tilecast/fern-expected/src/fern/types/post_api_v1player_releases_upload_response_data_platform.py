

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostApiV1PlayerReleasesUploadResponseDataPlatform(enum.StrEnum):
    ANDROID = "android"
    LINUX = "linux"

    def visit(self, android: typing.Callable[[], T_Result], linux: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostApiV1PlayerReleasesUploadResponseDataPlatform.ANDROID:
            return android()
        if self is PostApiV1PlayerReleasesUploadResponseDataPlatform.LINUX:
            return linux()
