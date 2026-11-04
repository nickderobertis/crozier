

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlayerUpdateMetadataPlatform(enum.StrEnum):
    ANDROID = "android"
    LINUX = "linux"

    def visit(self, android: typing.Callable[[], T_Result], linux: typing.Callable[[], T_Result]) -> T_Result:
        if self is PlayerUpdateMetadataPlatform.ANDROID:
            return android()
        if self is PlayerUpdateMetadataPlatform.LINUX:
            return linux()
