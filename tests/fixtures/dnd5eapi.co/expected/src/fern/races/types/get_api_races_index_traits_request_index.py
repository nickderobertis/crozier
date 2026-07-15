

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiRacesIndexTraitsRequestIndex(str, enum.Enum):
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
        if self is GetApiRacesIndexTraitsRequestIndex.DRAGONBORN:
            return dragonborn()
        if self is GetApiRacesIndexTraitsRequestIndex.DWARF:
            return dwarf()
        if self is GetApiRacesIndexTraitsRequestIndex.ELF:
            return elf()
        if self is GetApiRacesIndexTraitsRequestIndex.GNOME:
            return gnome()
        if self is GetApiRacesIndexTraitsRequestIndex.HALF_ELF:
            return half_elf()
        if self is GetApiRacesIndexTraitsRequestIndex.HALF_ORC:
            return half_orc()
        if self is GetApiRacesIndexTraitsRequestIndex.HALFLING:
            return halfling()
        if self is GetApiRacesIndexTraitsRequestIndex.HUMAN:
            return human()
        if self is GetApiRacesIndexTraitsRequestIndex.TIEFLING:
            return tiefling()
