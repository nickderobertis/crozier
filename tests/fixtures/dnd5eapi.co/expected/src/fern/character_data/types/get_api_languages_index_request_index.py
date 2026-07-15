

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiLanguagesIndexRequestIndex(str, enum.Enum):
    ABYSSAL = "abyssal"
    CELESTIAL = "celestial"
    COMMON = "common"
    DEEP_SPEECH = "deep-speech"
    DRACONIC = "draconic"
    DWARVISH = "dwarvish"
    ELVISH = "elvish"
    GIANT = "giant"
    GNOMISH = "gnomish"
    GOBLIN = "goblin"
    HALFLING = "halfling"
    INFERNAL = "infernal"
    ORC = "orc"
    PRIMORDIAL = "primordial"
    SYLVAN = "sylvan"
    UNDERCOMMON = "undercommon"

    def visit(
        self,
        abyssal: typing.Callable[[], T_Result],
        celestial: typing.Callable[[], T_Result],
        common: typing.Callable[[], T_Result],
        deep_speech: typing.Callable[[], T_Result],
        draconic: typing.Callable[[], T_Result],
        dwarvish: typing.Callable[[], T_Result],
        elvish: typing.Callable[[], T_Result],
        giant: typing.Callable[[], T_Result],
        gnomish: typing.Callable[[], T_Result],
        goblin: typing.Callable[[], T_Result],
        halfling: typing.Callable[[], T_Result],
        infernal: typing.Callable[[], T_Result],
        orc: typing.Callable[[], T_Result],
        primordial: typing.Callable[[], T_Result],
        sylvan: typing.Callable[[], T_Result],
        undercommon: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiLanguagesIndexRequestIndex.ABYSSAL:
            return abyssal()
        if self is GetApiLanguagesIndexRequestIndex.CELESTIAL:
            return celestial()
        if self is GetApiLanguagesIndexRequestIndex.COMMON:
            return common()
        if self is GetApiLanguagesIndexRequestIndex.DEEP_SPEECH:
            return deep_speech()
        if self is GetApiLanguagesIndexRequestIndex.DRACONIC:
            return draconic()
        if self is GetApiLanguagesIndexRequestIndex.DWARVISH:
            return dwarvish()
        if self is GetApiLanguagesIndexRequestIndex.ELVISH:
            return elvish()
        if self is GetApiLanguagesIndexRequestIndex.GIANT:
            return giant()
        if self is GetApiLanguagesIndexRequestIndex.GNOMISH:
            return gnomish()
        if self is GetApiLanguagesIndexRequestIndex.GOBLIN:
            return goblin()
        if self is GetApiLanguagesIndexRequestIndex.HALFLING:
            return halfling()
        if self is GetApiLanguagesIndexRequestIndex.INFERNAL:
            return infernal()
        if self is GetApiLanguagesIndexRequestIndex.ORC:
            return orc()
        if self is GetApiLanguagesIndexRequestIndex.PRIMORDIAL:
            return primordial()
        if self is GetApiLanguagesIndexRequestIndex.SYLVAN:
            return sylvan()
        if self is GetApiLanguagesIndexRequestIndex.UNDERCOMMON:
            return undercommon()
