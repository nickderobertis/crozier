

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActApproveRequestDecision(enum.StrEnum):
    APPROVE = "approve"
    REJECT = "reject"
    REQUEST_CHANGES = "request_changes"

    def visit(
        self,
        approve: typing.Callable[[], T_Result],
        reject: typing.Callable[[], T_Result],
        request_changes: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActApproveRequestDecision.APPROVE:
            return approve()
        if self is ActApproveRequestDecision.REJECT:
            return reject()
        if self is ActApproveRequestDecision.REQUEST_CHANGES:
            return request_changes()
