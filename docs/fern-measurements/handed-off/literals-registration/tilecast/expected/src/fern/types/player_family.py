

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlayerFamily(enum.StrEnum):
    """
    The Player release family. A deployment reaches only screens of its release's family, and for `edge` only screens of its architecture.
    """

    ANDROID = "android"
    ELECTRON_LINUX = "electron-linux"
    EDGE = "edge"

    def visit(
        self,
        android: typing.Callable[[], T_Result],
        electron_linux: typing.Callable[[], T_Result],
        edge: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlayerFamily.ANDROID:
            return android()
        if self is PlayerFamily.ELECTRON_LINUX:
            return electron_linux()
        if self is PlayerFamily.EDGE:
            return edge()
