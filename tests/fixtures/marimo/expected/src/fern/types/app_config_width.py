

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppConfigWidth(enum.StrEnum):
    COLUMNS = "columns"
    COMPACT = "compact"
    FULL = "full"
    MEDIUM = "medium"
    NORMAL = "normal"

    def visit(
        self,
        columns: typing.Callable[[], T_Result],
        compact: typing.Callable[[], T_Result],
        full: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        normal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppConfigWidth.COLUMNS:
            return columns()
        if self is AppConfigWidth.COMPACT:
            return compact()
        if self is AppConfigWidth.FULL:
            return full()
        if self is AppConfigWidth.MEDIUM:
            return medium()
        if self is AppConfigWidth.NORMAL:
            return normal()
