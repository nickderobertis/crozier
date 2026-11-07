

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NormPartyPartyClassificationType(enum.StrEnum):
    INDIVIDUAL = "Individual"
    ORGANIZATION = "Organization"

    def visit(self, individual: typing.Callable[[], T_Result], organization: typing.Callable[[], T_Result]) -> T_Result:
        if self is NormPartyPartyClassificationType.INDIVIDUAL:
            return individual()
        if self is NormPartyPartyClassificationType.ORGANIZATION:
            return organization()
