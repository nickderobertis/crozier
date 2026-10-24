

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentTaskRole(enum.StrEnum):
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
        if self is AgentTaskRole.EVIDENCE_ANALYST:
            return evidence_analyst()
        if self is AgentTaskRole.PLATFORM_SPECIALIST:
            return platform_specialist()
        if self is AgentTaskRole.CROSS_CONTROLLER:
            return cross_controller()
        if self is AgentTaskRole.MANAGER:
            return manager()
        if self is AgentTaskRole.REVIEWER:
            return reviewer()
