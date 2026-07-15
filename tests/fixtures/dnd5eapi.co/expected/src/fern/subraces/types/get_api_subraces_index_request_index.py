

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiSubracesIndexRequestIndex(str, enum.Enum):
    HIGH_ELF = "high-elf"
    HILL_DWARF = "hill-dwarf"
    LIGHTFOOT_HALFLING = "lightfoot-halfling"
    ROCK_GNOME = "rock-gnome"

    def visit(
        self,
        high_elf: typing.Callable[[], T_Result],
        hill_dwarf: typing.Callable[[], T_Result],
        lightfoot_halfling: typing.Callable[[], T_Result],
        rock_gnome: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiSubracesIndexRequestIndex.HIGH_ELF:
            return high_elf()
        if self is GetApiSubracesIndexRequestIndex.HILL_DWARF:
            return hill_dwarf()
        if self is GetApiSubracesIndexRequestIndex.LIGHTFOOT_HALFLING:
            return lightfoot_halfling()
        if self is GetApiSubracesIndexRequestIndex.ROCK_GNOME:
            return rock_gnome()
