

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageStatusMessengerStatus(enum.StrEnum):
    """
    The status of the message.
    """

    SUBMITTED = "submitted"
    DELIVERED = "delivered"
    REJECTED = "rejected"
    UNDELIVERABLE = "undeliverable"
    READ = "read"

    def visit(
        self,
        submitted: typing.Callable[[], T_Result],
        delivered: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        undeliverable: typing.Callable[[], T_Result],
        read: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageStatusMessengerStatus.SUBMITTED:
            return submitted()
        if self is MessageStatusMessengerStatus.DELIVERED:
            return delivered()
        if self is MessageStatusMessengerStatus.REJECTED:
            return rejected()
        if self is MessageStatusMessengerStatus.UNDELIVERABLE:
            return undeliverable()
        if self is MessageStatusMessengerStatus.READ:
            return read()
