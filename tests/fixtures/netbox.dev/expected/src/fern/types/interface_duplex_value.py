

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InterfaceDuplexValue(enum.StrEnum):
    HALF = "half"
    FULL = "full"
    AUTO = "auto"

    def visit(
        self,
        half: typing.Callable[[], T_Result],
        full: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InterfaceDuplexValue.HALF:
            return half()
        if self is InterfaceDuplexValue.FULL:
            return full()
        if self is InterfaceDuplexValue.AUTO:
            return auto()
