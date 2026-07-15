

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiMagicSchoolsIndexRequestIndex(str, enum.Enum):
    ABJURATION = "abjuration"
    CONJURATION = "conjuration"
    DIVINATION = "divination"
    ENCHANTMENT = "enchantment"
    EVOCATION = "evocation"
    ILLUSION = "illusion"
    NECROMANCY = "necromancy"
    TRANSMUTATION = "transmutation"

    def visit(
        self,
        abjuration: typing.Callable[[], T_Result],
        conjuration: typing.Callable[[], T_Result],
        divination: typing.Callable[[], T_Result],
        enchantment: typing.Callable[[], T_Result],
        evocation: typing.Callable[[], T_Result],
        illusion: typing.Callable[[], T_Result],
        necromancy: typing.Callable[[], T_Result],
        transmutation: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiMagicSchoolsIndexRequestIndex.ABJURATION:
            return abjuration()
        if self is GetApiMagicSchoolsIndexRequestIndex.CONJURATION:
            return conjuration()
        if self is GetApiMagicSchoolsIndexRequestIndex.DIVINATION:
            return divination()
        if self is GetApiMagicSchoolsIndexRequestIndex.ENCHANTMENT:
            return enchantment()
        if self is GetApiMagicSchoolsIndexRequestIndex.EVOCATION:
            return evocation()
        if self is GetApiMagicSchoolsIndexRequestIndex.ILLUSION:
            return illusion()
        if self is GetApiMagicSchoolsIndexRequestIndex.NECROMANCY:
            return necromancy()
        if self is GetApiMagicSchoolsIndexRequestIndex.TRANSMUTATION:
            return transmutation()
