

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentGraphVersionStatus(enum.StrEnum):
    DRAFT = "draft"
    PUBLISHED = "published"
    RETIRED = "retired"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        published: typing.Callable[[], T_Result],
        retired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgentGraphVersionStatus.DRAFT:
            return draft()
        if self is AgentGraphVersionStatus.PUBLISHED:
            return published()
        if self is AgentGraphVersionStatus.RETIRED:
            return retired()
