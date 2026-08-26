

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DisplayConfigDefaultWidth(enum.StrEnum):
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
        if self is DisplayConfigDefaultWidth.COLUMNS:
            return columns()
        if self is DisplayConfigDefaultWidth.COMPACT:
            return compact()
        if self is DisplayConfigDefaultWidth.FULL:
            return full()
        if self is DisplayConfigDefaultWidth.MEDIUM:
            return medium()
        if self is DisplayConfigDefaultWidth.NORMAL:
            return normal()
