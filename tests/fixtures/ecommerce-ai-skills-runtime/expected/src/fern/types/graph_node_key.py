

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GraphNodeKey(enum.StrEnum):
    EVIDENCE_ANALYST = "evidence_analyst"
    PLATFORM_SPECIALIST = "platform_specialist"
    CROSS_CONTROLLER = "cross_controller"
    MANAGER = "manager"
    REVIEWER = "reviewer"

    def visit(
        self,
        evidence_analyst: typing.Callable[[], T_Result],
        platform_specialist: typing.Callable[[], T_Result],
        cross_controller: typing.Callable[[], T_Result],
        manager: typing.Callable[[], T_Result],
        reviewer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GraphNodeKey.EVIDENCE_ANALYST:
            return evidence_analyst()
        if self is GraphNodeKey.PLATFORM_SPECIALIST:
            return platform_specialist()
        if self is GraphNodeKey.CROSS_CONTROLLER:
            return cross_controller()
        if self is GraphNodeKey.MANAGER:
            return manager()
        if self is GraphNodeKey.REVIEWER:
            return reviewer()
