

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SettingsUpdateDtoThumbnailSize(enum.StrEnum):
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
        if self is SettingsUpdateDtoThumbnailSize.DEFAULT:
            return default()
        if self is SettingsUpdateDtoThumbnailSize.MEDIUM:
            return medium()
        if self is SettingsUpdateDtoThumbnailSize.LARGE:
            return large()
        if self is SettingsUpdateDtoThumbnailSize.XLARGE:
            return xlarge()
