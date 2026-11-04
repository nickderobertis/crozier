

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolRelatedEntitiesItemRole(enum.StrEnum):
    """
    The manner of the relationship between the entity and the tool.
    """

    SUPPORTED_SCHEME = "supported scheme"
    MAINTAINER = "maintainer"
    FUNDER = "funder"

    def visit(
        self,
        supported_scheme: typing.Callable[[], T_Result],
        maintainer: typing.Callable[[], T_Result],
        funder: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ToolRelatedEntitiesItemRole.SUPPORTED_SCHEME:
            return supported_scheme()
        if self is ToolRelatedEntitiesItemRole.MAINTAINER:
            return maintainer()
        if self is ToolRelatedEntitiesItemRole.FUNDER:
            return funder()
