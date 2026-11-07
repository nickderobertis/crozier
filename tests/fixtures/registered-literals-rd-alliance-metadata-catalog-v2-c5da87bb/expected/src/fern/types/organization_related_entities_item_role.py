

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrganizationRelatedEntitiesItemRole(enum.StrEnum):
    """
    The manner of the relationship between the entity and the organization.
    """

    MAINTAINED_SCHEME = "maintained scheme"
    MAINTAINED_TOOL = "maintained tool"
    MAINTAINED_MAPPING = "maintained mapping"
    FUNDED_SCHEME = "funded scheme"
    FUNDED_TOOL = "funded tool"
    FUNDED_MAPPING = "funded mapping"
    USED_SCHEME = "used scheme"
    ENDORSEMENT = "endorsement"

    def visit(
        self,
        maintained_scheme: typing.Callable[[], T_Result],
        maintained_tool: typing.Callable[[], T_Result],
        maintained_mapping: typing.Callable[[], T_Result],
        funded_scheme: typing.Callable[[], T_Result],
        funded_tool: typing.Callable[[], T_Result],
        funded_mapping: typing.Callable[[], T_Result],
        used_scheme: typing.Callable[[], T_Result],
        endorsement: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrganizationRelatedEntitiesItemRole.MAINTAINED_SCHEME:
            return maintained_scheme()
        if self is OrganizationRelatedEntitiesItemRole.MAINTAINED_TOOL:
            return maintained_tool()
        if self is OrganizationRelatedEntitiesItemRole.MAINTAINED_MAPPING:
            return maintained_mapping()
        if self is OrganizationRelatedEntitiesItemRole.FUNDED_SCHEME:
            return funded_scheme()
        if self is OrganizationRelatedEntitiesItemRole.FUNDED_TOOL:
            return funded_tool()
        if self is OrganizationRelatedEntitiesItemRole.FUNDED_MAPPING:
            return funded_mapping()
        if self is OrganizationRelatedEntitiesItemRole.USED_SCHEME:
            return used_scheme()
        if self is OrganizationRelatedEntitiesItemRole.ENDORSEMENT:
            return endorsement()
