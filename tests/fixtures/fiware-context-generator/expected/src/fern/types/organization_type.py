

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrganizationType(enum.StrEnum):
    """
    NGSI entity type. It has to be Organization
    """

    ORGANIZATION = "Organization"

    def visit(self, organization: typing.Callable[[], T_Result]) -> T_Result:
        if self is OrganizationType.ORGANIZATION:
            return organization()
