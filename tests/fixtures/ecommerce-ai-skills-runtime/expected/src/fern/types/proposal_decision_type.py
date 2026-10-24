

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProposalDecisionType(enum.StrEnum):
    APPROVE = "approve"
    REJECT = "reject"
    REVISION_REQUIRED = "revision_required"

    def visit(
        self,
        approve: typing.Callable[[], T_Result],
        reject: typing.Callable[[], T_Result],
        revision_required: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProposalDecisionType.APPROVE:
            return approve()
        if self is ProposalDecisionType.REJECT:
            return reject()
        if self is ProposalDecisionType.REVISION_REQUIRED:
            return revision_required()
