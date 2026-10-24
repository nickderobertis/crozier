

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentArtifactKind(enum.StrEnum):
    INPUT_EVIDENCE = "input_evidence"
    SPECIALIST_FINDING = "specialist_finding"
    MANAGER_SYNTHESIS = "manager_synthesis"
    REVIEWER_VERDICT = "reviewer_verdict"
    WEEKLY_OPS_REPORT = "weekly_ops_report"

    def visit(
        self,
        input_evidence: typing.Callable[[], T_Result],
        specialist_finding: typing.Callable[[], T_Result],
        manager_synthesis: typing.Callable[[], T_Result],
        reviewer_verdict: typing.Callable[[], T_Result],
        weekly_ops_report: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgentArtifactKind.INPUT_EVIDENCE:
            return input_evidence()
        if self is AgentArtifactKind.SPECIALIST_FINDING:
            return specialist_finding()
        if self is AgentArtifactKind.MANAGER_SYNTHESIS:
            return manager_synthesis()
        if self is AgentArtifactKind.REVIEWER_VERDICT:
            return reviewer_verdict()
        if self is AgentArtifactKind.WEEKLY_OPS_REPORT:
            return weekly_ops_report()
