

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SettingsDtoThumbnailSize(enum.StrEnum):
    DEFAULT = "DEFAULT"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    XLARGE = "XLARGE"

    def visit(
        self,
        default: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        large: typing.Callable[[], T_Result],
        xlarge: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SettingsDtoThumbnailSize.DEFAULT:
            return default()
        if self is SettingsDtoThumbnailSize.MEDIUM:
            return medium()
        if self is SettingsDtoThumbnailSize.LARGE:
            return large()
        if self is SettingsDtoThumbnailSize.XLARGE:
            return xlarge()
