

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ShotSize(enum.StrEnum):
    WIDE = "wide"
    MEDIUM = "medium"
    CLOSE = "close"

    def visit(
        self,
        wide: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        close: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ShotSize.WIDE:
            return wide()
        if self is ShotSize.MEDIUM:
            return medium()
        if self is ShotSize.CLOSE:
            return close()
