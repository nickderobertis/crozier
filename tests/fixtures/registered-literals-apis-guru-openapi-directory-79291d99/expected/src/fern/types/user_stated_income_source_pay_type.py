

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserStatedIncomeSourcePayType(enum.StrEnum):
    """
    The pay type - `GROSS`, `NET`, or `UNKNOWN` for a specified income source
    """

    UNKNOWN = "UNKNOWN"
    GROSS = "GROSS"
    NET = "NET"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        gross: typing.Callable[[], T_Result],
        net: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserStatedIncomeSourcePayType.UNKNOWN:
            return unknown()
        if self is UserStatedIncomeSourcePayType.GROSS:
            return gross()
        if self is UserStatedIncomeSourcePayType.NET:
            return net()
