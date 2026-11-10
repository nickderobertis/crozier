

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DepositSwitchCreateRequestCountryCode(enum.StrEnum):
    """
    ISO-3166-1 alpha-2 country code standard.
    """

    US = "US"
    CA = "CA"

    def visit(self, us: typing.Callable[[], T_Result], ca: typing.Callable[[], T_Result]) -> T_Result:
        if self is DepositSwitchCreateRequestCountryCode.US:
            return us()
        if self is DepositSwitchCreateRequestCountryCode.CA:
            return ca()
