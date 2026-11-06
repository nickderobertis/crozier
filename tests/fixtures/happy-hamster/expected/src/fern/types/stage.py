

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Stage(enum.StrEnum):
    """
    Stages
    """

    NOVICE = "novice"
    EXPLORER = "explorer"
    PRO = "pro"
    EXPERT = "expert"
    HERO = "hero"

    def visit(
        self,
        novice: typing.Callable[[], T_Result],
        explorer: typing.Callable[[], T_Result],
        pro: typing.Callable[[], T_Result],
        expert: typing.Callable[[], T_Result],
        hero: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Stage.NOVICE:
            return novice()
        if self is Stage.EXPLORER:
            return explorer()
        if self is Stage.PRO:
            return pro()
        if self is Stage.EXPERT:
            return expert()
        if self is Stage.HERO:
            return hero()
