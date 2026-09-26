

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LayoutConfig(enum.StrEnum):
    """
    @deprecated Always uses stretch layout.
    """

    AUTO = "auto"
    STRETCH = "stretch"

    def visit(self, auto: typing.Callable[[], T_Result], stretch: typing.Callable[[], T_Result]) -> T_Result:
        if self is LayoutConfig.AUTO:
            return auto()
        if self is LayoutConfig.STRETCH:
            return stretch()
