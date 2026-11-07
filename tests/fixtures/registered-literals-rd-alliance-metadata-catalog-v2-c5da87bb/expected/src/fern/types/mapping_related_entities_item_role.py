

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MappingRelatedEntitiesItemRole(enum.StrEnum):
    """
    The manner of the relationship between the entity and the mapping.
    """

    INPUT_SCHEME = "input scheme"
    OUTPUT_SCHEME = "output scheme"
    MAINTAINER = "maintainer"
    FUNDER = "funder"

    def visit(
        self,
        input_scheme: typing.Callable[[], T_Result],
        output_scheme: typing.Callable[[], T_Result],
        maintainer: typing.Callable[[], T_Result],
        funder: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MappingRelatedEntitiesItemRole.INPUT_SCHEME:
            return input_scheme()
        if self is MappingRelatedEntitiesItemRole.OUTPUT_SCHEME:
            return output_scheme()
        if self is MappingRelatedEntitiesItemRole.MAINTAINER:
            return maintainer()
        if self is MappingRelatedEntitiesItemRole.FUNDER:
            return funder()
