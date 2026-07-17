

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MonsterReactionsItemActionsItemType(enum.StrEnum):
    MELEE = "melee"
    RANGED = "ranged"
    ABILITY = "ability"
    MAGIC = "magic"

    def visit(
        self,
        melee: typing.Callable[[], T_Result],
        ranged: typing.Callable[[], T_Result],
        ability: typing.Callable[[], T_Result],
        magic: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonsterReactionsItemActionsItemType.MELEE:
            return melee()
        if self is MonsterReactionsItemActionsItemType.RANGED:
            return ranged()
        if self is MonsterReactionsItemActionsItemType.ABILITY:
            return ability()
        if self is MonsterReactionsItemActionsItemType.MAGIC:
            return magic()
