

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GameGetGamesRequestChipsetVariant(enum.StrEnum):
    BASE = "BASE"
    PRO = "PRO"
    MAX = "MAX"
    ULTRA = "ULTRA"

    def visit(
        self,
        base: typing.Callable[[], T_Result],
        pro: typing.Callable[[], T_Result],
        max: typing.Callable[[], T_Result],
        ultra: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GameGetGamesRequestChipsetVariant.BASE:
            return base()
        if self is GameGetGamesRequestChipsetVariant.PRO:
            return pro()
        if self is GameGetGamesRequestChipsetVariant.MAX:
            return max()
        if self is GameGetGamesRequestChipsetVariant.ULTRA:
            return ultra()
