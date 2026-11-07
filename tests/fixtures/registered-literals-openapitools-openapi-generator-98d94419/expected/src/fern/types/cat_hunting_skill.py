

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatHuntingSkill(enum.StrEnum):
    """
    The measured skill for hunting
    """

    CLUELESS = "clueless"
    LAZY = "lazy"
    ADVENTUROUS = "adventurous"
    AGGRESSIVE = "aggressive"

    def visit(
        self,
        clueless: typing.Callable[[], T_Result],
        lazy: typing.Callable[[], T_Result],
        adventurous: typing.Callable[[], T_Result],
        aggressive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CatHuntingSkill.CLUELESS:
            return clueless()
        if self is CatHuntingSkill.LAZY:
            return lazy()
        if self is CatHuntingSkill.ADVENTUROUS:
            return adventurous()
        if self is CatHuntingSkill.AGGRESSIVE:
            return aggressive()
