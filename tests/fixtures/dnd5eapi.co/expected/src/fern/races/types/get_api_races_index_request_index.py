

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiRacesIndexRequestIndex(str, enum.Enum):
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
        if self is GetApiRacesIndexRequestIndex.DRAGONBORN:
            return dragonborn()
        if self is GetApiRacesIndexRequestIndex.DWARF:
            return dwarf()
        if self is GetApiRacesIndexRequestIndex.ELF:
            return elf()
        if self is GetApiRacesIndexRequestIndex.GNOME:
            return gnome()
        if self is GetApiRacesIndexRequestIndex.HALF_ELF:
            return half_elf()
        if self is GetApiRacesIndexRequestIndex.HALF_ORC:
            return half_orc()
        if self is GetApiRacesIndexRequestIndex.HALFLING:
            return halfling()
        if self is GetApiRacesIndexRequestIndex.HUMAN:
            return human()
        if self is GetApiRacesIndexRequestIndex.TIEFLING:
            return tiefling()
