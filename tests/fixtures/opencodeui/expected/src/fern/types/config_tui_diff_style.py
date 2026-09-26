

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConfigTuiDiffStyle(enum.StrEnum):
    """
    Control diff rendering style: 'auto' adapts to terminal width, 'stacked' always shows single column
    """

    AUTO = "auto"
    STACKED = "stacked"

    def visit(self, auto: typing.Callable[[], T_Result], stacked: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConfigTuiDiffStyle.AUTO:
            return auto()
        if self is ConfigTuiDiffStyle.STACKED:
            return stacked()
