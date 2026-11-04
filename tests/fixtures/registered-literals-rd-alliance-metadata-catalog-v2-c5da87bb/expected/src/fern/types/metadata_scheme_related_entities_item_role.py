

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetadataSchemeRelatedEntitiesItemRole(enum.StrEnum):
    """
    The manner of the relationship between the entity and the scheme.
    """

    PARENT_SCHEME = "parent scheme"
    CHILD_SCHEME = "child scheme"
    INPUT_TO_MAPPING = "input to mapping"
    OUTPUT_FROM_MAPPING = "output from mapping"
    MAINTAINER = "maintainer"
    FUNDER = "funder"
    USER = "user"
    TOOL = "tool"
    ENDORSEMENT = "endorsement"

    def visit(
        self,
        parent_scheme: typing.Callable[[], T_Result],
        child_scheme: typing.Callable[[], T_Result],
        input_to_mapping: typing.Callable[[], T_Result],
        output_from_mapping: typing.Callable[[], T_Result],
        maintainer: typing.Callable[[], T_Result],
        funder: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        tool: typing.Callable[[], T_Result],
        endorsement: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MetadataSchemeRelatedEntitiesItemRole.PARENT_SCHEME:
            return parent_scheme()
        if self is MetadataSchemeRelatedEntitiesItemRole.CHILD_SCHEME:
            return child_scheme()
        if self is MetadataSchemeRelatedEntitiesItemRole.INPUT_TO_MAPPING:
            return input_to_mapping()
        if self is MetadataSchemeRelatedEntitiesItemRole.OUTPUT_FROM_MAPPING:
            return output_from_mapping()
        if self is MetadataSchemeRelatedEntitiesItemRole.MAINTAINER:
            return maintainer()
        if self is MetadataSchemeRelatedEntitiesItemRole.FUNDER:
            return funder()
        if self is MetadataSchemeRelatedEntitiesItemRole.USER:
            return user()
        if self is MetadataSchemeRelatedEntitiesItemRole.TOOL:
            return tool()
        if self is MetadataSchemeRelatedEntitiesItemRole.ENDORSEMENT:
            return endorsement()
