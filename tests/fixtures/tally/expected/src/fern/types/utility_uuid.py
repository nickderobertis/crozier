

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UtilityUuid(enum.StrEnum):
    """
    Identifier used as uuid and blockGroupUuid for utility field references.
    """

    UTILITY_TODAY = "utility::today()"

    def visit(self, utility_today: typing.Callable[[], T_Result]) -> T_Result:
        if self is UtilityUuid.UTILITY_TODAY:
            return utility_today()
