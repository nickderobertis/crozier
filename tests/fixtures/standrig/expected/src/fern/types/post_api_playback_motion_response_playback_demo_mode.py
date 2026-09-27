

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostApiPlaybackMotionResponsePlaybackDemoMode(enum.StrEnum):
    SHOWCASE_ACTIVE = "showcase-active"
    MOUSE_EXPRESSION = "mouse-expression"

    def visit(
        self, showcase_active: typing.Callable[[], T_Result], mouse_expression: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PostApiPlaybackMotionResponsePlaybackDemoMode.SHOWCASE_ACTIVE:
            return showcase_active()
        if self is PostApiPlaybackMotionResponsePlaybackDemoMode.MOUSE_EXPRESSION:
            return mouse_expression()
