

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppConfigLayout(enum.StrEnum):
    """
    Section layout
    """

    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
    AUTO = "auto"
    MASONRY = "masonry"
    SIDEBAR = "sidebar"

    def visit(
        self,
        horizontal: typing.Callable[[], T_Result],
        vertical: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
        masonry: typing.Callable[[], T_Result],
        sidebar: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppConfigLayout.HORIZONTAL:
            return horizontal()
        if self is AppConfigLayout.VERTICAL:
            return vertical()
        if self is AppConfigLayout.AUTO:
            return auto()
        if self is AppConfigLayout.MASONRY:
            return masonry()
        if self is AppConfigLayout.SIDEBAR:
            return sidebar()
