

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentTaskVerificationStatus(enum.StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    VERIFIED = "verified"
    MISMATCH = "mismatch"
    UNVERIFIABLE = "unverifiable"
    ERROR = "error"
    UNSUPPORTED = "unsupported"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        verified: typing.Callable[[], T_Result],
        mismatch: typing.Callable[[], T_Result],
        unverifiable: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        unsupported: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgentTaskVerificationStatus.PENDING:
            return pending()
        if self is AgentTaskVerificationStatus.RUNNING:
            return running()
        if self is AgentTaskVerificationStatus.VERIFIED:
            return verified()
        if self is AgentTaskVerificationStatus.MISMATCH:
            return mismatch()
        if self is AgentTaskVerificationStatus.UNVERIFIABLE:
            return unverifiable()
        if self is AgentTaskVerificationStatus.ERROR:
            return error()
        if self is AgentTaskVerificationStatus.UNSUPPORTED:
            return unsupported()
