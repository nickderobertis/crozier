

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NormOrganizationOrganizationType(enum.StrEnum):
    BUSINESS = "Business"
    GOVERNMENT_AGENCY = "GovernmentAgency"

    def visit(
        self, business: typing.Callable[[], T_Result], government_agency: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is NormOrganizationOrganizationType.BUSINESS:
            return business()
        if self is NormOrganizationOrganizationType.GOVERNMENT_AGENCY:
            return government_agency()
