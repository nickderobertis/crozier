

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlaylistItemInputDeliveryPolicy(enum.StrEnum):
    DOWNLOAD = "download"
    STREAM = "stream"
    AUTOMATIC = "automatic"

    def visit(
        self,
        download: typing.Callable[[], T_Result],
        stream: typing.Callable[[], T_Result],
        automatic: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlaylistItemInputDeliveryPolicy.DOWNLOAD:
            return download()
        if self is PlaylistItemInputDeliveryPolicy.STREAM:
            return stream()
        if self is PlaylistItemInputDeliveryPolicy.AUTOMATIC:
            return automatic()
