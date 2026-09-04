

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderRelationshipRelationshipType(enum.StrEnum):
    PRIMARY_WEALTH_MANAGER = "primary_wealth_manager"
    CUSTODY_SERVICES = "custody_services"
    ADVISORY_ONLY = "advisory_only"

    def visit(
        self,
        primary_wealth_manager: typing.Callable[[], T_Result],
        custody_services: typing.Callable[[], T_Result],
        advisory_only: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProviderRelationshipRelationshipType.PRIMARY_WEALTH_MANAGER:
            return primary_wealth_manager()
        if self is ProviderRelationshipRelationshipType.CUSTODY_SERVICES:
            return custody_services()
        if self is ProviderRelationshipRelationshipType.ADVISORY_ONLY:
            return advisory_only()
