

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GameGetGamesRequestChipset(enum.StrEnum):
    A18 = "A18"
    M1 = "M1"
    M2 = "M2"
    M3 = "M3"
    M4 = "M4"
    M5 = "M5"

    def visit(
        self,
        a18: typing.Callable[[], T_Result],
        m1: typing.Callable[[], T_Result],
        m2: typing.Callable[[], T_Result],
        m3: typing.Callable[[], T_Result],
        m4: typing.Callable[[], T_Result],
        m5: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GameGetGamesRequestChipset.A18:
            return a18()
        if self is GameGetGamesRequestChipset.M1:
            return m1()
        if self is GameGetGamesRequestChipset.M2:
            return m2()
        if self is GameGetGamesRequestChipset.M3:
            return m3()
        if self is GameGetGamesRequestChipset.M4:
            return m4()
        if self is GameGetGamesRequestChipset.M5:
            return m5()
