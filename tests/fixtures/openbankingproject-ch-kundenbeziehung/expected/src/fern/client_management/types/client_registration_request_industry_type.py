

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ClientRegistrationRequestIndustryType(enum.StrEnum):
    BANKING = "banking"
    INSURANCE = "insurance"
    FINTECH = "fintech"
    OTHER = "other"

    def visit(
        self,
        banking: typing.Callable[[], T_Result],
        insurance: typing.Callable[[], T_Result],
        fintech: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientRegistrationRequestIndustryType.BANKING:
            return banking()
        if self is ClientRegistrationRequestIndustryType.INSURANCE:
            return insurance()
        if self is ClientRegistrationRequestIndustryType.FINTECH:
            return fintech()
        if self is ClientRegistrationRequestIndustryType.OTHER:
            return other()
