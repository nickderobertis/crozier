

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GraphNodeInstructionKey(enum.StrEnum):
    WEEKLY_OPS_EVIDENCE_ANALYST_V1 = "weekly_ops.evidence_analyst.v1"
    WEEKLY_OPS_PLATFORM_SPECIALIST_V1 = "weekly_ops.platform_specialist.v1"
    WEEKLY_OPS_CROSS_CONTROLLER_V1 = "weekly_ops.cross_controller.v1"
    WEEKLY_OPS_MANAGER_V1 = "weekly_ops.manager.v1"
    WEEKLY_OPS_REVIEWER_V1 = "weekly_ops.reviewer.v1"

    def visit(
        self,
        weekly_ops_evidence_analyst_v1: typing.Callable[[], T_Result],
        weekly_ops_platform_specialist_v1: typing.Callable[[], T_Result],
        weekly_ops_cross_controller_v1: typing.Callable[[], T_Result],
        weekly_ops_manager_v1: typing.Callable[[], T_Result],
        weekly_ops_reviewer_v1: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GraphNodeInstructionKey.WEEKLY_OPS_EVIDENCE_ANALYST_V1:
            return weekly_ops_evidence_analyst_v1()
        if self is GraphNodeInstructionKey.WEEKLY_OPS_PLATFORM_SPECIALIST_V1:
            return weekly_ops_platform_specialist_v1()
        if self is GraphNodeInstructionKey.WEEKLY_OPS_CROSS_CONTROLLER_V1:
            return weekly_ops_cross_controller_v1()
        if self is GraphNodeInstructionKey.WEEKLY_OPS_MANAGER_V1:
            return weekly_ops_manager_v1()
        if self is GraphNodeInstructionKey.WEEKLY_OPS_REVIEWER_V1:
            return weekly_ops_reviewer_v1()
