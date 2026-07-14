

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiRacesIndexProficienciesRequestIndex(str, enum.Enum):
    DRAGONBORN = "dragonborn"
    DWARF = "dwarf"
    ELF = "elf"
    GNOME = "gnome"
    HALF_ELF = "half-elf"
    HALF_ORC = "half-orc"
    HALFLING = "halfling"
    HUMAN = "human"
    TIEFLING = "tiefling"

    def visit(
        self,
        dragonborn: typing.Callable[[], T_Result],
        dwarf: typing.Callable[[], T_Result],
        elf: typing.Callable[[], T_Result],
        gnome: typing.Callable[[], T_Result],
        half_elf: typing.Callable[[], T_Result],
        half_orc: typing.Callable[[], T_Result],
        halfling: typing.Callable[[], T_Result],
        human: typing.Callable[[], T_Result],
        tiefling: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiRacesIndexProficienciesRequestIndex.DRAGONBORN:
            return dragonborn()
        if self is GetApiRacesIndexProficienciesRequestIndex.DWARF:
            return dwarf()
        if self is GetApiRacesIndexProficienciesRequestIndex.ELF:
            return elf()
        if self is GetApiRacesIndexProficienciesRequestIndex.GNOME:
            return gnome()
        if self is GetApiRacesIndexProficienciesRequestIndex.HALF_ELF:
            return half_elf()
        if self is GetApiRacesIndexProficienciesRequestIndex.HALF_ORC:
            return half_orc()
        if self is GetApiRacesIndexProficienciesRequestIndex.HALFLING:
            return halfling()
        if self is GetApiRacesIndexProficienciesRequestIndex.HUMAN:
            return human()
        if self is GetApiRacesIndexProficienciesRequestIndex.TIEFLING:
            return tiefling()
