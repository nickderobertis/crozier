

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PartyPartyClassificationType(enum.StrEnum):
    """
    To know the type of an entity in a case, if it is an Individual, Company or Other. An entity to a case could be the parties, attorneys or judges involved.
    """

    INDIVIDUAL = "INDIVIDUAL"
    COMPANY = "COMPANY"
    OTHER = "OTHER"

    def visit(
        self,
        individual: typing.Callable[[], T_Result],
        company: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PartyPartyClassificationType.INDIVIDUAL:
            return individual()
        if self is PartyPartyClassificationType.COMPANY:
            return company()
        if self is PartyPartyClassificationType.OTHER:
            return other()
