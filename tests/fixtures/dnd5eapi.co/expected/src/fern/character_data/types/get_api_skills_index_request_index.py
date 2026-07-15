

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiSkillsIndexRequestIndex(str, enum.Enum):
    ACROBATICS = "acrobatics"
    ANIMAL_HANDLING = "animal-handling"
    ARCANA = "arcana"
    ATHLETICS = "athletics"
    DECEPTION = "deception"
    HISTORY = "history"
    INSIGHT = "insight"
    INTIMIDATION = "intimidation"
    INVESTIGATION = "investigation"
    MEDICINE = "medicine"
    NATURE = "nature"
    PERCEPTION = "perception"
    PERFORMANCE = "performance"
    PERSUASION = "persuasion"
    RELIGION = "religion"
    SLEIGHT_OF_HAND = "sleight-of-hand"
    STEALTH = "stealth"
    SURVIVAL = "survival"

    def visit(
        self,
        acrobatics: typing.Callable[[], T_Result],
        animal_handling: typing.Callable[[], T_Result],
        arcana: typing.Callable[[], T_Result],
        athletics: typing.Callable[[], T_Result],
        deception: typing.Callable[[], T_Result],
        history: typing.Callable[[], T_Result],
        insight: typing.Callable[[], T_Result],
        intimidation: typing.Callable[[], T_Result],
        investigation: typing.Callable[[], T_Result],
        medicine: typing.Callable[[], T_Result],
        nature: typing.Callable[[], T_Result],
        perception: typing.Callable[[], T_Result],
        performance: typing.Callable[[], T_Result],
        persuasion: typing.Callable[[], T_Result],
        religion: typing.Callable[[], T_Result],
        sleight_of_hand: typing.Callable[[], T_Result],
        stealth: typing.Callable[[], T_Result],
        survival: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiSkillsIndexRequestIndex.ACROBATICS:
            return acrobatics()
        if self is GetApiSkillsIndexRequestIndex.ANIMAL_HANDLING:
            return animal_handling()
        if self is GetApiSkillsIndexRequestIndex.ARCANA:
            return arcana()
        if self is GetApiSkillsIndexRequestIndex.ATHLETICS:
            return athletics()
        if self is GetApiSkillsIndexRequestIndex.DECEPTION:
            return deception()
        if self is GetApiSkillsIndexRequestIndex.HISTORY:
            return history()
        if self is GetApiSkillsIndexRequestIndex.INSIGHT:
            return insight()
        if self is GetApiSkillsIndexRequestIndex.INTIMIDATION:
            return intimidation()
        if self is GetApiSkillsIndexRequestIndex.INVESTIGATION:
            return investigation()
        if self is GetApiSkillsIndexRequestIndex.MEDICINE:
            return medicine()
        if self is GetApiSkillsIndexRequestIndex.NATURE:
            return nature()
        if self is GetApiSkillsIndexRequestIndex.PERCEPTION:
            return perception()
        if self is GetApiSkillsIndexRequestIndex.PERFORMANCE:
            return performance()
        if self is GetApiSkillsIndexRequestIndex.PERSUASION:
            return persuasion()
        if self is GetApiSkillsIndexRequestIndex.RELIGION:
            return religion()
        if self is GetApiSkillsIndexRequestIndex.SLEIGHT_OF_HAND:
            return sleight_of_hand()
        if self is GetApiSkillsIndexRequestIndex.STEALTH:
            return stealth()
        if self is GetApiSkillsIndexRequestIndex.SURVIVAL:
            return survival()
