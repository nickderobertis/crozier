

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiRacesIndexSubracesRequestIndex(str, enum.Enum):
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
        if self is GetApiRacesIndexSubracesRequestIndex.DRAGONBORN:
            return dragonborn()
        if self is GetApiRacesIndexSubracesRequestIndex.DWARF:
            return dwarf()
        if self is GetApiRacesIndexSubracesRequestIndex.ELF:
            return elf()
        if self is GetApiRacesIndexSubracesRequestIndex.GNOME:
            return gnome()
        if self is GetApiRacesIndexSubracesRequestIndex.HALF_ELF:
            return half_elf()
        if self is GetApiRacesIndexSubracesRequestIndex.HALF_ORC:
            return half_orc()
        if self is GetApiRacesIndexSubracesRequestIndex.HALFLING:
            return halfling()
        if self is GetApiRacesIndexSubracesRequestIndex.HUMAN:
            return human()
        if self is GetApiRacesIndexSubracesRequestIndex.TIEFLING:
            return tiefling()
