

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageStatusBaseStatus(enum.StrEnum):
    """
    The status of the message.
    """

    SUBMITTED = "submitted"
    DELIVERED = "delivered"
    REJECTED = "rejected"
    UNDELIVERABLE = "undeliverable"

    def visit(
        self,
        submitted: typing.Callable[[], T_Result],
        delivered: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        undeliverable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageStatusBaseStatus.SUBMITTED:
            return submitted()
        if self is MessageStatusBaseStatus.DELIVERED:
            return delivered()
        if self is MessageStatusBaseStatus.REJECTED:
            return rejected()
        if self is MessageStatusBaseStatus.UNDELIVERABLE:
            return undeliverable()
