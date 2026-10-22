

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppConfigIconSize(enum.StrEnum):
    """
    Item icon size
    """

    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

    def visit(
        self,
        small: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        large: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppConfigIconSize.SMALL:
            return small()
        if self is AppConfigIconSize.MEDIUM:
            return medium()
        if self is AppConfigIconSize.LARGE:
            return large()
