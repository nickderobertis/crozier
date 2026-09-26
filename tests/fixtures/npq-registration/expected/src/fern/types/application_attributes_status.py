

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApplicationAttributesStatus(enum.StrEnum):
    """
    The current state of the NPQ application
    """

    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        accepted: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApplicationAttributesStatus.PENDING:
            return pending()
        if self is ApplicationAttributesStatus.ACCEPTED:
            return accepted()
        if self is ApplicationAttributesStatus.REJECTED:
            return rejected()
