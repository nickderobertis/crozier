

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GameMode(enum.StrEnum):
    """
    A game mode supported by codosseum
    """

    FASTEST = "fastest"
    REVERSE = "reverse"
    GOLF = "golf"
    ARCADE = "arcade"
    BATTLE_ROYALE = "battleRoyale"

    def visit(
        self,
        fastest: typing.Callable[[], T_Result],
        reverse: typing.Callable[[], T_Result],
        golf: typing.Callable[[], T_Result],
        arcade: typing.Callable[[], T_Result],
        battle_royale: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GameMode.FASTEST:
            return fastest()
        if self is GameMode.REVERSE:
            return reverse()
        if self is GameMode.GOLF:
            return golf()
        if self is GameMode.ARCADE:
            return arcade()
        if self is GameMode.BATTLE_ROYALE:
            return battle_royale()
