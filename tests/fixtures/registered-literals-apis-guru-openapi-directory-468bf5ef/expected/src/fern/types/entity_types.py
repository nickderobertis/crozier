

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntityTypes(enum.StrEnum):
    """
    An enumeration.
    """

    GOVERNMENT = "government"
    COMMUNITY = "community"
    RESEARCH = "research"

    def visit(
        self,
        government: typing.Callable[[], T_Result],
        community: typing.Callable[[], T_Result],
        research: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntityTypes.GOVERNMENT:
            return government()
        if self is EntityTypes.COMMUNITY:
            return community()
        if self is EntityTypes.RESEARCH:
            return research()
