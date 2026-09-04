

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StatusCode(enum.StrEnum):
    """
    The code for the status of the grant. Possible values:
    - **Pending**
    - **Active**
    - **Repaid**
    - **WrittenOff**
    - **Failed**
    - **Revoked**
    - **Requested**
    - **Reviewing**
    - **Approved**
    - **Rejected**
    - **Cancelled**
    """

    PENDING = "Pending"
    ACTIVE = "Active"
    REPAID = "Repaid"
    WRITTEN_OFF = "WrittenOff"
    FAILED = "Failed"
    REVOKED = "Revoked"
    REQUESTED = "Requested"
    REVIEWING = "Reviewing"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    CANCELLED = "Cancelled"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        repaid: typing.Callable[[], T_Result],
        written_off: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        revoked: typing.Callable[[], T_Result],
        requested: typing.Callable[[], T_Result],
        reviewing: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StatusCode.PENDING:
            return pending()
        if self is StatusCode.ACTIVE:
            return active()
        if self is StatusCode.REPAID:
            return repaid()
        if self is StatusCode.WRITTEN_OFF:
            return written_off()
        if self is StatusCode.FAILED:
            return failed()
        if self is StatusCode.REVOKED:
            return revoked()
        if self is StatusCode.REQUESTED:
            return requested()
        if self is StatusCode.REVIEWING:
            return reviewing()
        if self is StatusCode.APPROVED:
            return approved()
        if self is StatusCode.REJECTED:
            return rejected()
        if self is StatusCode.CANCELLED:
            return cancelled()
