

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OptionActionNameType(enum.StrEnum):
    """
    For attack options that can be melee, ranged, abilities, or thrown.
    """

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
        if self is OptionActionNameType.MELEE:
            return melee()
        if self is OptionActionNameType.RANGED:
            return ranged()
        if self is OptionActionNameType.ABILITY:
            return ability()
        if self is OptionActionNameType.MAGIC:
            return magic()
