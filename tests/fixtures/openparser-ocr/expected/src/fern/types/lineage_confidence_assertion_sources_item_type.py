

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LineageConfidenceAssertionSourcesItemType(enum.StrEnum):
    ENTITY = "entity"
    ACTIVITY = "activity"
    AGENT = "agent"

    def visit(
        self,
        entity: typing.Callable[[], T_Result],
        activity: typing.Callable[[], T_Result],
        agent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LineageConfidenceAssertionSourcesItemType.ENTITY:
            return entity()
        if self is LineageConfidenceAssertionSourcesItemType.ACTIVITY:
            return activity()
        if self is LineageConfidenceAssertionSourcesItemType.AGENT:
            return agent()
