

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiRulesIndexRequestIndex(str, enum.Enum):
    ADVENTURING = "adventuring"
    APPENDIX = "appendix"
    COMBAT = "combat"
    EQUIPMENT = "equipment"
    SPELLCASTING = "spellcasting"
    USING_ABILITY_SCORES = "using-ability-scores"

    def visit(
        self,
        adventuring: typing.Callable[[], T_Result],
        appendix: typing.Callable[[], T_Result],
        combat: typing.Callable[[], T_Result],
        equipment: typing.Callable[[], T_Result],
        spellcasting: typing.Callable[[], T_Result],
        using_ability_scores: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiRulesIndexRequestIndex.ADVENTURING:
            return adventuring()
        if self is GetApiRulesIndexRequestIndex.APPENDIX:
            return appendix()
        if self is GetApiRulesIndexRequestIndex.COMBAT:
            return combat()
        if self is GetApiRulesIndexRequestIndex.EQUIPMENT:
            return equipment()
        if self is GetApiRulesIndexRequestIndex.SPELLCASTING:
            return spellcasting()
        if self is GetApiRulesIndexRequestIndex.USING_ABILITY_SCORES:
            return using_ability_scores()
