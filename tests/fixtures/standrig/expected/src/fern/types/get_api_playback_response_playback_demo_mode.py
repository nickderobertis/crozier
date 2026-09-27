

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiPlaybackResponsePlaybackDemoMode(enum.StrEnum):
    SHOWCASE_ACTIVE = "showcase-active"
    MOUSE_EXPRESSION = "mouse-expression"

    def visit(
        self, showcase_active: typing.Callable[[], T_Result], mouse_expression: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is GetApiPlaybackResponsePlaybackDemoMode.SHOWCASE_ACTIVE:
            return showcase_active()
        if self is GetApiPlaybackResponsePlaybackDemoMode.MOUSE_EXPRESSION:
            return mouse_expression()
