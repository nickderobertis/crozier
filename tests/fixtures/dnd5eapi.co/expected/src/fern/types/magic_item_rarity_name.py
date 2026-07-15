

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MagicItemRarityName(str, enum.Enum):
    """
    The rarity of the item.
    """

    VARIES = "Varies"
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    VERY_RARE = "Very Rare"
    LEGENDARY = "Legendary"
    ARTIFACT = "Artifact"

    def visit(
        self,
        varies: typing.Callable[[], T_Result],
        common: typing.Callable[[], T_Result],
        uncommon: typing.Callable[[], T_Result],
        rare: typing.Callable[[], T_Result],
        very_rare: typing.Callable[[], T_Result],
        legendary: typing.Callable[[], T_Result],
        artifact: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MagicItemRarityName.VARIES:
            return varies()
        if self is MagicItemRarityName.COMMON:
            return common()
        if self is MagicItemRarityName.UNCOMMON:
            return uncommon()
        if self is MagicItemRarityName.RARE:
            return rare()
        if self is MagicItemRarityName.VERY_RARE:
            return very_rare()
        if self is MagicItemRarityName.LEGENDARY:
            return legendary()
        if self is MagicItemRarityName.ARTIFACT:
            return artifact()
