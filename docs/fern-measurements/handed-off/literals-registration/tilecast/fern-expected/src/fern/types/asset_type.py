

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssetType(enum.StrEnum):
    IMAGE = "image"
    VIDEO = "video"
    WIDGET = "widget"

    def visit(
        self,
        image: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
        widget: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssetType.IMAGE:
            return image()
        if self is AssetType.VIDEO:
            return video()
        if self is AssetType.WIDGET:
            return widget()
