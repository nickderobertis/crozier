

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantIndustry(enum.StrEnum):
    BANKING = "banking"
    INSURANCE = "insurance"
    REAL_ESTATE = "real_estate"
    MOBILITY = "mobility"
    RETAIL = "retail"
    GOVERNMENT = "government"

    def visit(
        self,
        banking: typing.Callable[[], T_Result],
        insurance: typing.Callable[[], T_Result],
        real_estate: typing.Callable[[], T_Result],
        mobility: typing.Callable[[], T_Result],
        retail: typing.Callable[[], T_Result],
        government: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ParticipantIndustry.BANKING:
            return banking()
        if self is ParticipantIndustry.INSURANCE:
            return insurance()
        if self is ParticipantIndustry.REAL_ESTATE:
            return real_estate()
        if self is ParticipantIndustry.MOBILITY:
            return mobility()
        if self is ParticipantIndustry.RETAIL:
            return retail()
        if self is ParticipantIndustry.GOVERNMENT:
            return government()
