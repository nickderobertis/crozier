

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiAbilityScoresIndexRequestIndex(str, enum.Enum):
    CHA = "cha"
    CON = "con"
    DEX = "dex"
    INT = "int"
    STR = "str"
    WIS = "wis"

    def visit(
        self,
        cha: typing.Callable[[], T_Result],
        con: typing.Callable[[], T_Result],
        dex: typing.Callable[[], T_Result],
        int_: typing.Callable[[], T_Result],
        str: typing.Callable[[], T_Result],
        wis: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiAbilityScoresIndexRequestIndex.CHA:
            return cha()
        if self is GetApiAbilityScoresIndexRequestIndex.CON:
            return con()
        if self is GetApiAbilityScoresIndexRequestIndex.DEX:
            return dex()
        if self is GetApiAbilityScoresIndexRequestIndex.INT:
            return int_()
        if self is GetApiAbilityScoresIndexRequestIndex.STR:
            return str()
        if self is GetApiAbilityScoresIndexRequestIndex.WIS:
            return wis()
