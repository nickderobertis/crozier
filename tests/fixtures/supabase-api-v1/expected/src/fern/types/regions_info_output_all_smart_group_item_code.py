

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RegionsInfoOutputAllSmartGroupItemCode(enum.StrEnum):
    AMERICAS = "americas"
    EMEA = "emea"
    APAC = "apac"

    def visit(
        self,
        americas: typing.Callable[[], T_Result],
        emea: typing.Callable[[], T_Result],
        apac: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RegionsInfoOutputAllSmartGroupItemCode.AMERICAS:
            return americas()
        if self is RegionsInfoOutputAllSmartGroupItemCode.EMEA:
            return emea()
        if self is RegionsInfoOutputAllSmartGroupItemCode.APAC:
            return apac()
