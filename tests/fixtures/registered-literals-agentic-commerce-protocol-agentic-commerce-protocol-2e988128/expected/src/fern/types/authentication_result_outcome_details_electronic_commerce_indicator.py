

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationResultOutcomeDetailsElectronicCommerceIndicator(enum.StrEnum):
    """
    Electronic Commerce Indicator (ECI) returned by the 3D Secure provider. Indicates the degree/type of authentication performed.
    """

    ONE = "01"
    TWO = "02"
    FIVE = "05"
    SIX = "06"
    SEVEN = "07"

    def visit(
        self,
        one: typing.Callable[[], T_Result],
        two: typing.Callable[[], T_Result],
        five: typing.Callable[[], T_Result],
        six: typing.Callable[[], T_Result],
        seven: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthenticationResultOutcomeDetailsElectronicCommerceIndicator.ONE:
            return one()
        if self is AuthenticationResultOutcomeDetailsElectronicCommerceIndicator.TWO:
            return two()
        if self is AuthenticationResultOutcomeDetailsElectronicCommerceIndicator.FIVE:
            return five()
        if self is AuthenticationResultOutcomeDetailsElectronicCommerceIndicator.SIX:
            return six()
        if self is AuthenticationResultOutcomeDetailsElectronicCommerceIndicator.SEVEN:
            return seven()
