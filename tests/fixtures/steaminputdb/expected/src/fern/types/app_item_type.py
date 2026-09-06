

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppItemType(enum.StrEnum):
    GAME = "game"
    DEMO = "demo"
    MOD = "mod"

    def visit(
        self,
        game: typing.Callable[[], T_Result],
        demo: typing.Callable[[], T_Result],
        mod: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppItemType.GAME:
            return game()
        if self is AppItemType.DEMO:
            return demo()
        if self is AppItemType.MOD:
            return mod()
