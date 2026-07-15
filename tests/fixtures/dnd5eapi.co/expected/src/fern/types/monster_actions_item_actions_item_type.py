

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MonsterActionsItemActionsItemType(str, enum.Enum):
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
        if self is MonsterActionsItemActionsItemType.MELEE:
            return melee()
        if self is MonsterActionsItemActionsItemType.RANGED:
            return ranged()
        if self is MonsterActionsItemActionsItemType.ABILITY:
            return ability()
        if self is MonsterActionsItemActionsItemType.MAGIC:
            return magic()
