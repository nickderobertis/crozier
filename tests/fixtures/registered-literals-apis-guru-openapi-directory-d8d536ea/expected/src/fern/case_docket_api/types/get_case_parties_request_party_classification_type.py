

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCasePartiesRequestPartyClassificationType(enum.StrEnum):
    INDIVIDUAL = "INDIVIDUAL"
    COMPANY = "COMPANY"
    OTHER = "OTHER"

    def visit(
        self,
        individual: typing.Callable[[], T_Result],
        company: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetCasePartiesRequestPartyClassificationType.INDIVIDUAL:
            return individual()
        if self is GetCasePartiesRequestPartyClassificationType.COMPANY:
            return company()
        if self is GetCasePartiesRequestPartyClassificationType.OTHER:
            return other()
