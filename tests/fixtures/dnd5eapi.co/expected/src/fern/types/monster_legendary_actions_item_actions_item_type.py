

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MonsterLegendaryActionsItemActionsItemType(str, enum.Enum):
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
        if self is MonsterLegendaryActionsItemActionsItemType.MELEE:
            return melee()
        if self is MonsterLegendaryActionsItemActionsItemType.RANGED:
            return ranged()
        if self is MonsterLegendaryActionsItemActionsItemType.ABILITY:
            return ability()
        if self is MonsterLegendaryActionsItemActionsItemType.MAGIC:
            return magic()
