

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PresentationOverrideInputTargetType(enum.StrEnum):
    SCREEN = "screen"
    GROUP = "group"

    def visit(self, screen: typing.Callable[[], T_Result], group: typing.Callable[[], T_Result]) -> T_Result:
        if self is PresentationOverrideInputTargetType.SCREEN:
            return screen()
        if self is PresentationOverrideInputTargetType.GROUP:
            return group()
