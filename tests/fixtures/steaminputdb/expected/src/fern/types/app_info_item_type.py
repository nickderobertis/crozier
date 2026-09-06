

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppInfoItemType(enum.StrEnum):
    GAME = "game"
    DEMO = "demo"
    MOD = "mod"

    def visit(
        self,
        game: typing.Callable[[], T_Result],
        demo: typing.Callable[[], T_Result],
        mod: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppInfoItemType.GAME:
            return game()
        if self is AppInfoItemType.DEMO:
            return demo()
        if self is AppInfoItemType.MOD:
            return mod()
